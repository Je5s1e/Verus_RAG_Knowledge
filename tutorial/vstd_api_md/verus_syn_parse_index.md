<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)

</div>

# Module parse Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/parse.rs.html#1-1434"
class="src">Source</a> </span>

</div>

Expand description

<div class="docblock">

Parsing interface for parsing a token stream into a syntax tree node.

Parsing in Syn is built on parser functions that take in a
[`ParseStream`](type.ParseStream.html "type verus_syn::parse::ParseStream")
and produce a
[`Result<T>`](../type.Result.html "type verus_syn::Result") where `T` is
some syntax tree node. Underlying these parser functions is a lower
level mechanism built around the
[`Cursor`](../buffer/struct.Cursor.html "struct verus_syn::buffer::Cursor")
type. `Cursor` is a cheaply copyable cursor over a range of tokens in a
token stream.

## <a href="#example" class="doc-anchor">§</a>Example

Here is a snippet of parsing code to get a feel for the style of the
library. We define data structures for a subset of Rust syntax including
enums (not shown) and structs, then provide implementations of the
[`Parse`](trait.Parse.html "trait verus_syn::parse::Parse") trait to
parse these syntax tree data structures from a token stream.

Once `Parse` impls have been defined, they can be called conveniently
from a procedural macro through
[`parse_macro_input!`](../macro.parse_macro_input.html "macro verus_syn::parse_macro_input")
as shown at the bottom of the snippet. If the caller provides
syntactically invalid input to the procedural macro, they will receive a
helpful compiler error message pointing out the exact token that
triggered the failure to parse.

<div class="example-wrap">

``` rust
use proc_macro::TokenStream;
use syn::{braced, parse_macro_input, token, Field, Ident, Result, Token};
use syn::parse::{Parse, ParseStream};
use syn::punctuated::Punctuated;

enum Item {
    Struct(ItemStruct),
    Enum(ItemEnum),
}

struct ItemStruct {
    struct_token: Token![struct],
    ident: Ident,
    brace_token: token::Brace,
    fields: Punctuated<Field, Token![,]>,
}

impl Parse for Item {
    fn parse(input: ParseStream) -> Result<Self> {
        let lookahead = input.lookahead1();
        if lookahead.peek(Token![struct]) {
            input.parse().map(Item::Struct)
        } else if lookahead.peek(Token![enum]) {
            input.parse().map(Item::Enum)
        } else {
            Err(lookahead.error())
        }
    }
}

impl Parse for ItemStruct {
    fn parse(input: ParseStream) -> Result<Self> {
        let content;
        Ok(ItemStruct {
            struct_token: input.parse()?,
            ident: input.parse()?,
            brace_token: braced!(content in input),
            fields: content.parse_terminated(Field::parse_named, Token![,])?,
        })
    }
}

#[proc_macro]
pub fn my_macro(tokens: TokenStream) -> TokenStream {
    let input = parse_macro_input!(tokens as Item);

    /* ... */
}
```

</div>

## <a href="#the-synparse-functions" class="doc-anchor">§</a>The `syn::parse*` functions

The [`syn::parse`](../fn.parse.html "fn verus_syn::parse"),
[`syn::parse2`](../fn.parse2.html "fn verus_syn::parse2"), and
[`syn::parse_str`](../fn.parse_str.html "fn verus_syn::parse_str")
functions serve as an entry point for parsing syntax tree nodes that can
be parsed in an obvious default way. These functions can return any
syntax tree node that implements the
[`Parse`](trait.Parse.html "trait verus_syn::parse::Parse") trait, which
includes most types in Syn.

<div class="example-wrap">

``` rust
use syn::Type;

let t: Type = syn::parse_str("std::collections::HashMap<String, Value>")?;
```

</div>

The
[`parse_quote!`](../macro.parse_quote.html "macro verus_syn::parse_quote")
macro also uses this approach.

## <a href="#the-parser-trait" class="doc-anchor">§</a>The `Parser` trait

Some types can be parsed in several ways depending on context. For
example an
[`Attribute`](../struct.Attribute.html "struct verus_syn::Attribute")
can be either “outer” like `#[...]` or “inner” like `#![...]` and
parsing the wrong one would be a bug. Similarly
[`Punctuated`](../punctuated/index.html "mod verus_syn::punctuated") may
or may not allow trailing punctuation, and parsing it the wrong way
would either reject valid input or accept invalid input.

The `Parse` trait is not implemented in these cases because there is no
good behavior to consider the default.

<div class="example-wrap compile_fail">

<a href="#" class="tooltip"
title="This example deliberately fails to compile">ⓘ</a>

``` rust
// Can't parse `Punctuated` without knowing whether trailing punctuation
// should be allowed in this context.
let path: Punctuated<PathSegment, Token![::]> = syn::parse(tokens)?;
```

</div>

In these cases the types provide a choice of parser functions rather
than a single `Parse` implementation, and those parser functions can be
invoked through the
[`Parser`](trait.Parser.html "trait verus_syn::parse::Parser") trait.

<div class="example-wrap">

``` rust
use proc_macro::TokenStream;
use syn::parse::Parser;
use syn::punctuated::Punctuated;
use syn::{Attribute, Expr, PathSegment, Result, Token};

fn call_some_parser_methods(input: TokenStream) -> Result<()> {
    // Parse a nonempty sequence of path segments separated by `::` punctuation
    // with no trailing punctuation.
    let tokens = input.clone();
    let parser = Punctuated::<PathSegment, Token![::]>::parse_separated_nonempty;
    let _path = parser.parse(tokens)?;

    // Parse a possibly empty sequence of expressions terminated by commas with
    // an optional trailing punctuation.
    let tokens = input.clone();
    let parser = Punctuated::<Expr, Token![,]>::parse_terminated;
    let _args = parser.parse(tokens)?;

    // Parse zero or more outer attributes but not inner attributes.
    let tokens = input.clone();
    let parser = Attribute::parse_outer;
    let _attrs = parser.parse(tokens)?;

    Ok(())
}
```

</div>

</div>

## Modules<a href="#modules" class="anchor">§</a>

<a href="discouraged/index.html" class="mod"
title="mod verus_syn::parse::discouraged">discouraged</a>  
Extensions to the parsing API with niche applicability.

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.End.html" class="struct"
title="struct verus_syn::parse::End">End</a>  
Pseudo-token used for peeking the end of a parse stream.

<a href="struct.Error.html" class="struct"
title="struct verus_syn::parse::Error">Error</a>  
Error returned when a Syn parser cannot parse the input tokens.

<a href="struct.Lookahead1.html" class="struct"
title="struct verus_syn::parse::Lookahead1">Lookahead1</a>  
Support for checking the next token in a stream to decide how to parse.

<a href="struct.Nothing.html" class="struct"
title="struct verus_syn::parse::Nothing">Nothing</a>  
An empty syntax tree node that consumes no tokens when parsed.

<a href="struct.ParseBuffer.html" class="struct"
title="struct verus_syn::parse::ParseBuffer">ParseBuffer</a>  
Cursor position within a buffered token stream.

<a href="struct.StepCursor.html" class="struct"
title="struct verus_syn::parse::StepCursor">StepCursor</a>  
Cursor state associated with speculative parsing.

## Traits<a href="#traits" class="anchor">§</a>

<a href="trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a>  
Parsing interface implemented by all types that can be parsed in a
default way from a token stream.

<a href="trait.Parser.html" class="trait"
title="trait verus_syn::parse::Parser">Parser</a>  
Parser that can parse Rust tokens into a particular syntax tree node.

<a href="trait.Peek.html" class="trait"
title="trait verus_syn::parse::Peek">Peek</a>  
Types that can be parsed by looking at just one token.

## Type Aliases<a href="#types" class="anchor">§</a>

<a href="type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>  
Input to a Syn parser function.

<a href="type.Result.html" class="type"
title="type verus_syn::parse::Result">Result</a>  
The result of a Syn parser.

</div>

</div>
