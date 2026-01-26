<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](../index.html)::[parse](index.html)

</div>

# Struct <span class="struct">ParseBuffer</span> Copy item path

<span class="sub-heading"><a href="../../src/syn/parse.rs.html#247-263" class="src">Source</a>
</span>

</div>

``` rust
pub struct ParseBuffer<'a> { /* private fields */ }
```

Expand description

<div class="docblock">

Cursor position within a buffered token stream.

This type is more commonly used through the type alias
[`ParseStream`](type.ParseStream.html "type syn::parse::ParseStream")
which is an alias for `&ParseBuffer`.

`ParseStream` is the input type for all parser functions in Syn. They
have the signature `fn(ParseStream) -> Result<T>`.

### <a href="#calling-a-parser-function" class="doc-anchor">§</a>Calling a parser function

There is no public way to construct a `ParseBuffer`. Instead, if you are
looking to invoke a parser function that requires `ParseStream` as
input, you will need to go through one of the public parsing entry
points.

- The
  [`parse_macro_input!`](../macro.parse_macro_input.html "macro syn::parse_macro_input")
  macro if parsing input of a procedural macro;
- One of [the `syn::parse*`
  functions](index.html#the-synparse-functions "mod syn::parse"); or
- A method of the
  [`Parser`](trait.Parser.html "trait syn::parse::Parser") trait.

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-ParseBuffer%3C'a%3E" class="section impl">

<a href="../../src/syn/parse.rs.html#463-1164"
class="src rightside">Source</a><a href="#impl-ParseBuffer%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="struct.ParseBuffer.html" class="struct"
title="struct syn::parse::ParseBuffer">ParseBuffer</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.parse" class="section method">

<a href="../../src/syn/parse.rs.html#466-468"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse" class="fn">parse</a>\<T: <a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a>\>(&self) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<T\>

</div>

<div class="docblock">

Parses a syntax tree node of type `T`, advancing the position of our
parse stream past it.

</div>

<div id="method.call" class="section method">

<a href="../../src/syn/parse.rs.html#506-508"
class="src rightside">Source</a>

#### pub fn <a href="#method.call" class="fn">call</a>\<T\>( &'a self, function: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.fn.html"
class="primitive">fn</a>(<a href="type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'a\>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<T\>, ) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<T\>

</div>

<div class="docblock">

Calls the given parser function to parse a syntax tree node of type `T`
from this stream.

##### <a href="#example" class="doc-anchor">§</a>Example

The parser below invokes
[`Attribute::parse_outer`](../struct.Attribute.html#method.parse_outer "associated function syn::Attribute::parse_outer")
to parse a vector of zero or more outer attributes.

<div class="example-wrap">

``` rust
use syn::{Attribute, Ident, Result, Token};
use syn::parse::{Parse, ParseStream};

// Parses a unit struct with attributes.
//
//     #[path = "s.tmpl"]
//     struct S;
struct UnitStruct {
    attrs: Vec<Attribute>,
    struct_token: Token![struct],
    name: Ident,
    semi_token: Token![;],
}

impl Parse for UnitStruct {
    fn parse(input: ParseStream) -> Result<Self> {
        Ok(UnitStruct {
            attrs: input.call(Attribute::parse_outer)?,
            struct_token: input.parse()?,
            name: input.parse()?,
            semi_token: input.parse()?,
        })
    }
}
```

</div>

</div>

<div id="method.peek" class="section method">

<a href="../../src/syn/parse.rs.html#582-585"
class="src rightside">Source</a>

#### pub fn <a href="#method.peek" class="fn">peek</a>\<T: <a href="trait.Peek.html" class="trait"
title="trait syn::parse::Peek">Peek</a>\>(&self, token: T) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Looks at the next token in the parse stream to determine whether it
matches the requested type of token.

Does not advance the position of the parse stream.

##### <a href="#syntax" class="doc-anchor">§</a>Syntax

Note that this method does not use turbofish syntax. Pass the peek type
inside of parentheses.

- `input.peek(Token![struct])`
- `input.peek(Token![==])`
- `input.peek(syn::Ident)` *(does not accept keywords)*
- `input.peek(syn::Ident::peek_any)`
- `input.peek(Lifetime)`
- `input.peek(token::Brace)`

##### <a href="#example-1" class="doc-anchor">§</a>Example

In this example we finish parsing the list of supertraits when the next
token in the input is either `where` or an opening curly brace.

<div class="example-wrap">

``` rust
use syn::{braced, token, Generics, Ident, Result, Token, TypeParamBound};
use syn::parse::{Parse, ParseStream};
use syn::punctuated::Punctuated;

// Parses a trait definition containing no associated items.
//
//     trait Marker<'de, T>: A + B<'de> where Box<T>: Clone {}
struct MarkerTrait {
    trait_token: Token![trait],
    ident: Ident,
    generics: Generics,
    colon_token: Option<Token![:]>,
    supertraits: Punctuated<TypeParamBound, Token![+]>,
    brace_token: token::Brace,
}

impl Parse for MarkerTrait {
    fn parse(input: ParseStream) -> Result<Self> {
        let trait_token: Token![trait] = input.parse()?;
        let ident: Ident = input.parse()?;
        let mut generics: Generics = input.parse()?;
        let colon_token: Option<Token![:]> = input.parse()?;

        let mut supertraits = Punctuated::new();
        if colon_token.is_some() {
            loop {
                supertraits.push_value(input.parse()?);
                if input.peek(Token![where]) || input.peek(token::Brace) {
                    break;
                }
                supertraits.push_punct(input.parse()?);
            }
        }

        generics.where_clause = input.parse()?;
        let content;
        let empty_brace_token = braced!(content in input);

        Ok(MarkerTrait {
            trait_token,
            ident,
            generics,
            colon_token,
            supertraits,
            brace_token: empty_brace_token,
        })
    }
}
```

</div>

</div>

<div id="method.peek2" class="section method">

<a href="../../src/syn/parse.rs.html#621-628"
class="src rightside">Source</a>

#### pub fn <a href="#method.peek2" class="fn">peek2</a>\<T: <a href="trait.Peek.html" class="trait"
title="trait syn::parse::Peek">Peek</a>\>(&self, token: T) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Looks at the second-next token in the parse stream.

This is commonly useful as a way to implement contextual keywords.

##### <a href="#example-2" class="doc-anchor">§</a>Example

This example needs to use `peek2` because the symbol `union` is not a
keyword in Rust. We can’t use just `peek` and decide to parse a union if
the very next token is `union`, because someone is free to write a
`mod union` and a macro invocation that looks like
`union::some_macro! { ... }`. In other words `union` is a contextual
keyword.

<div class="example-wrap">

``` rust
use syn::{Ident, ItemUnion, Macro, Result, Token};
use syn::parse::{Parse, ParseStream};

// Parses either a union or a macro invocation.
enum UnionOrMacro {
    // union MaybeUninit<T> { uninit: (), value: T }
    Union(ItemUnion),
    // lazy_static! { ... }
    Macro(Macro),
}

impl Parse for UnionOrMacro {
    fn parse(input: ParseStream) -> Result<Self> {
        if input.peek(Token![union]) && input.peek2(Ident) {
            input.parse().map(UnionOrMacro::Union)
        } else {
            input.parse().map(UnionOrMacro::Macro)
        }
    }
}
```

</div>

</div>

<div id="method.peek3" class="section method">

<a href="../../src/syn/parse.rs.html#631-642"
class="src rightside">Source</a>

#### pub fn <a href="#method.peek3" class="fn">peek3</a>\<T: <a href="trait.Peek.html" class="trait"
title="trait syn::parse::Peek">Peek</a>\>(&self, token: T) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Looks at the third-next token in the parse stream.

</div>

<div id="method.parse_terminated" class="section method">

<a href="../../src/syn/parse.rs.html#735-746"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse_terminated" class="fn">parse_terminated</a>\<T, P\>( &'a self, parser: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.fn.html"
class="primitive">fn</a>(<a href="type.ParseStream.html" class="type"
title="type syn::parse::ParseStream">ParseStream</a>\<'a\>) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<T\>, separator: P, ) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<<a href="../punctuated/struct.Punctuated.html" class="struct"
title="struct syn::punctuated::Punctuated">Punctuated</a>\<T, P::<a href="trait.Peek.html#associatedtype.Token" class="associatedtype"
title="type syn::parse::Peek::Token">Token</a>\>\>

<div class="where">

where P: <a href="trait.Peek.html" class="trait"
title="trait syn::parse::Peek">Peek</a>,
P::<a href="trait.Peek.html#associatedtype.Token" class="associatedtype"
title="type syn::parse::Peek::Token">Token</a>:
<a href="trait.Parse.html" class="trait"
title="trait syn::parse::Parse">Parse</a>,

</div>

</div>

<div class="docblock">

Parses zero or more occurrences of `T` separated by punctuation of type
`P`, with optional trailing punctuation.

Parsing continues until the end of this parse stream. The entire content
of this parse stream must consist of `T` and `P`.

##### <a href="#example-3" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use syn::{parenthesized, token, Ident, Result, Token, Type};
use syn::parse::{Parse, ParseStream};
use syn::punctuated::Punctuated;

// Parse a simplified tuple struct syntax like:
//
//     struct S(A, B);
struct TupleStruct {
    struct_token: Token![struct],
    ident: Ident,
    paren_token: token::Paren,
    fields: Punctuated<Type, Token![,]>,
    semi_token: Token![;],
}

impl Parse for TupleStruct {
    fn parse(input: ParseStream) -> Result<Self> {
        let content;
        Ok(TupleStruct {
            struct_token: input.parse()?,
            ident: input.parse()?,
            paren_token: parenthesized!(content in input),
            fields: content.parse_terminated(Type::parse, Token![,])?,
            semi_token: input.parse()?,
        })
    }
}
```

</div>

##### <a href="#see-also" class="doc-anchor">§</a>See also

If your separator is anything more complicated than an invocation of the
`Token!` macro, this method won’t be applicable and you can instead
directly use `Punctuated`’s parser functions:
[`parse_terminated`](../punctuated/struct.Punctuated.html#method.parse_terminated "associated function syn::punctuated::Punctuated::parse_terminated"),
[`parse_separated_nonempty`](../punctuated/struct.Punctuated.html#method.parse_separated_nonempty "associated function syn::punctuated::Punctuated::parse_separated_nonempty")
etc.

<div class="example-wrap">

``` rust
use syn::{custom_keyword, Expr, Result, Token};
use syn::parse::{Parse, ParseStream};
use syn::punctuated::Punctuated;

mod kw {
    syn::custom_keyword!(fin);
}

struct Fin(kw::fin, Token![;]);

impl Parse for Fin {
    fn parse(input: ParseStream) -> Result<Self> {
        Ok(Self(input.parse()?, input.parse()?))
    }
}

struct Thing {
    steps: Punctuated<Expr, Fin>,
}

impl Parse for Thing {
    fn parse(input: ParseStream) -> Result<Self> {
        Ok(Thing {
            steps: Punctuated::parse_terminated(input)?,
        })
        // or equivalently, this means the same thing:
            steps: input.call(Punctuated::parse_terminated)?,
    }
}
```

</div>

</div>

<div id="method.is_empty" class="section method">

<a href="../../src/syn/parse.rs.html#792-794"
class="src rightside">Source</a>

#### pub fn <a href="#method.is_empty" class="fn">is_empty</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Returns whether there are no more tokens remaining to be parsed from
this stream.

This method returns true upon reaching the end of the content within a
set of delimiters, as well as at the end of the tokens provided to the
outermost parsing entry point.

This is equivalent to
`.`[`peek`](#method.peek)`(`[`syn::parse::End`](struct.End.html)`)`. Use
`.peek2(End)` or `.peek3(End)` to look for the end of a parse stream
further ahead than the current position.

##### <a href="#example-4" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use syn::{braced, token, Ident, Item, Result, Token};
use syn::parse::{Parse, ParseStream};

// Parses a Rust `mod m { ... }` containing zero or more items.
struct Mod {
    mod_token: Token![mod],
    name: Ident,
    brace_token: token::Brace,
    items: Vec<Item>,
}

impl Parse for Mod {
    fn parse(input: ParseStream) -> Result<Self> {
        let content;
        Ok(Mod {
            mod_token: input.parse()?,
            name: input.parse()?,
            brace_token: braced!(content in input),
            items: {
                let mut items = Vec::new();
                while !content.is_empty() {
                    items.push(content.parse()?);
                }
                items
            },
        })
    }
}
```

</div>

</div>

<div id="method.lookahead1" class="section method">

<a href="../../src/syn/parse.rs.html#837-839"
class="src rightside">Source</a>

#### pub fn <a href="#method.lookahead1" class="fn">lookahead1</a>(&self) -\> <a href="struct.Lookahead1.html" class="struct"
title="struct syn::parse::Lookahead1">Lookahead1</a>\<'a\>

</div>

<div class="docblock">

Constructs a helper for peeking at the next token in this stream and
building an error message if it is not one of a set of expected tokens.

##### <a href="#example-5" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use syn::{ConstParam, Ident, Lifetime, LifetimeParam, Result, Token, TypeParam};
use syn::parse::{Parse, ParseStream};

// A generic parameter, a single one of the comma-separated elements inside
// angle brackets in:
//
//     fn f<T: Clone, 'a, 'b: 'a, const N: usize>() { ... }
//
// On invalid input, lookahead gives us a reasonable error message.
//
//     error: expected one of: identifier, lifetime, `const`
//       |
//     5 |     fn f<!Sized>() {}
//       |          ^
enum GenericParam {
    Type(TypeParam),
    Lifetime(LifetimeParam),
    Const(ConstParam),
}

impl Parse for GenericParam {
    fn parse(input: ParseStream) -> Result<Self> {
        let lookahead = input.lookahead1();
        if lookahead.peek(Ident) {
            input.parse().map(GenericParam::Type)
        } else if lookahead.peek(Lifetime) {
            input.parse().map(GenericParam::Lifetime)
        } else if lookahead.peek(Token![const]) {
            input.parse().map(GenericParam::Const)
        } else {
            Err(lookahead.error())
        }
    }
}
```

</div>

</div>

<div id="method.fork" class="section method">

<a href="../../src/syn/parse.rs.html#967-976"
class="src rightside">Source</a>

#### pub fn <a href="#method.fork" class="fn">fork</a>(&self) -\> Self

</div>

<div class="docblock">

Forks a parse stream so that parsing tokens out of either the original
or the fork does not advance the position of the other.

##### <a href="#performance" class="doc-anchor">§</a>Performance

Forking a parse stream is a cheap fixed amount of work and does not
involve copying token buffers. Where you might hit performance problems
is if your macro ends up parsing a large amount of content more than
once.

<div class="example-wrap">

``` rust
// Do not do this.
if input.fork().parse::<Expr>().is_ok() {
    return input.parse::<Expr>();
}
```

</div>

As a rule, avoid parsing an unbounded amount of tokens out of a forked
parse stream. Only use a fork when the amount of work performed against
the fork is small and bounded.

When complex speculative parsing against the forked stream is
unavoidable, use
[`parse::discouraged::Speculative`](discouraged/trait.Speculative.html "trait syn::parse::discouraged::Speculative")
to advance the original stream once the fork’s parse is determined to
have been successful.

For a lower level way to perform speculative parsing at the token level,
consider using
[`ParseStream::step`](struct.ParseBuffer.html#method.step "method syn::parse::ParseBuffer::step")
instead.

##### <a href="#example-6" class="doc-anchor">§</a>Example

The parse implementation shown here parses possibly restricted `pub`
visibilities.

- `pub`
- `pub(crate)`
- `pub(self)`
- `pub(super)`
- `pub(in some::path)`

To handle the case of visibilities inside of tuple structs, the parser
needs to distinguish parentheses that specify visibility restrictions
from parentheses that form part of a tuple type.

<div class="example-wrap">

``` rust
struct S(pub(crate) A, pub (B, C));
```

</div>

In this example input the first tuple struct element of `S` has
`pub(crate)` visibility while the second tuple struct element has `pub`
visibility; the parentheses around `(B, C)` are part of the type rather
than part of a visibility restriction.

The parser uses a forked parse stream to check the first token inside of
parentheses after the `pub` keyword. This is a small bounded amount of
work performed against the forked parse stream.

<div class="example-wrap">

``` rust
use syn::{parenthesized, token, Ident, Path, Result, Token};
use syn::ext::IdentExt;
use syn::parse::{Parse, ParseStream};

struct PubVisibility {
    pub_token: Token![pub],
    restricted: Option<Restricted>,
}

struct Restricted {
    paren_token: token::Paren,
    in_token: Option<Token![in]>,
    path: Path,
}

impl Parse for PubVisibility {
    fn parse(input: ParseStream) -> Result<Self> {
        let pub_token: Token![pub] = input.parse()?;

        if input.peek(token::Paren) {
            let ahead = input.fork();
            let mut content;
            parenthesized!(content in ahead);

            if content.peek(Token![crate])
                || content.peek(Token![self])
                || content.peek(Token![super])
            {
                return Ok(PubVisibility {
                    pub_token,
                    restricted: Some(Restricted {
                        paren_token: parenthesized!(content in input),
                        in_token: None,
                        path: Path::from(content.call(Ident::parse_any)?),
                    }),
                });
            } else if content.peek(Token![in]) {
                return Ok(PubVisibility {
                    pub_token,
                    restricted: Some(Restricted {
                        paren_token: parenthesized!(content in input),
                        in_token: Some(content.parse()?),
                        path: content.call(Path::parse_mod_style)?,
                    }),
                });
            }
        }

        Ok(PubVisibility {
            pub_token,
            restricted: None,
        })
    }
}
```

</div>

</div>

<div id="method.error" class="section method">

<a href="../../src/syn/parse.rs.html#1006-1008"
class="src rightside">Source</a>

#### pub fn <a href="#method.error" class="fn">error</a>\<T: <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html"
class="trait" title="trait core::fmt::Display">Display</a>\>(&self, message: T) -\> <a href="../struct.Error.html" class="struct"
title="struct syn::Error">Error</a>

</div>

<div class="docblock">

Triggers an error at the current position of the parse stream.

##### <a href="#example-7" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use syn::{Expr, Result, Token};
use syn::parse::{Parse, ParseStream};

// Some kind of loop: `while` or `for` or `loop`.
struct Loop {
    expr: Expr,
}

impl Parse for Loop {
    fn parse(input: ParseStream) -> Result<Self> {
        if input.peek(Token![while])
            || input.peek(Token![for])
            || input.peek(Token![loop])
        {
            Ok(Loop {
                expr: input.parse()?,
            })
        } else {
            Err(input.error("expected some kind of loop"))
        }
    }
}
```

</div>

</div>

<div id="method.step" class="section method">

<a href="../../src/syn/parse.rs.html#1055-1083"
class="src rightside">Source</a>

#### pub fn <a href="#method.step" class="fn">step</a>\<F, R\>(&self, function: F) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<R\>

<div class="where">

where F: for\<'c\> <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnOnce.html"
class="trait" title="trait core::ops::function::FnOnce">FnOnce</a>(<a href="struct.StepCursor.html" class="struct"
title="struct syn::parse::StepCursor">StepCursor</a>\<'c, 'a\>) -\>
<a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<(R,
<a href="../buffer/struct.Cursor.html" class="struct"
title="struct syn::buffer::Cursor">Cursor</a>\<'c\>)\>,

</div>

</div>

<div class="docblock">

Speculatively parses tokens from this parse stream, advancing the
position of this stream only if parsing succeeds.

This is a powerful low-level API used for defining the `Parse` impls of
the basic built-in token types. It is not something that will be used
widely outside of the Syn codebase.

##### <a href="#example-8" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use proc_macro2::TokenTree;
use syn::Result;
use syn::parse::ParseStream;

// This function advances the stream past the next occurrence of `@`. If
// no `@` is present in the stream, the stream position is unchanged and
// an error is returned.
fn skip_past_next_at(input: ParseStream) -> Result<()> {
    input.step(|cursor| {
        let mut rest = *cursor;
        while let Some((tt, next)) = rest.token_tree() {
            match &tt {
                TokenTree::Punct(punct) if punct.as_char() == '@' => {
                    return Ok(((), next));
                }
                _ => rest = next,
            }
        }
        Err(cursor.error("no `@` was found after this point"))
    })
}
```

</div>

</div>

<div id="method.span" class="section method">

<a href="../../src/syn/parse.rs.html#1088-1095"
class="src rightside">Source</a>

#### pub fn <a href="#method.span" class="fn">span</a>(&self) -\> <a href="../../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="docblock">

Returns the `Span` of the next token in the parse stream, or
`Span::call_site()` if this parse stream has completely exhausted its
input `TokenStream`.

</div>

<div id="method.cursor" class="section method">

<a href="../../src/syn/parse.rs.html#1154-1156"
class="src rightside">Source</a>

#### pub fn <a href="#method.cursor" class="fn">cursor</a>(&self) -\> <a href="../buffer/struct.Cursor.html" class="struct"
title="struct syn::buffer::Cursor">Cursor</a>\<'a\>

</div>

<div class="docblock">

Provides low-level access to the token representation underlying this
parse stream.

Cursors are immutable so no operations you perform against the cursor
will affect the state of this parse stream.

##### <a href="#example-9" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use proc_macro2::TokenStream;
use syn::buffer::Cursor;
use syn::parse::{ParseStream, Result};

// Run a parser that returns T, but get its output as TokenStream instead of T.
// This works without T needing to implement ToTokens.
fn recognize_token_stream<T>(
    recognizer: fn(ParseStream) -> Result<T>,
) -> impl Fn(ParseStream) -> Result<TokenStream> {
    move |input| {
        let begin = input.cursor();
        recognizer(input)?;
        let end = input.cursor();
        Ok(tokens_between(begin, end))
    }
}

// Collect tokens between two cursors as a TokenStream.
fn tokens_between(begin: Cursor, end: Cursor) -> TokenStream {
    assert!(begin <= end);

    let mut cursor = begin;
    let mut tokens = TokenStream::new();
    while cursor < end {
        let (token, next) = cursor.token_tree().unwrap();
        tokens.extend(core::iter::once(token));
        cursor = next;
    }
    tokens
}

fn main() {
    use quote::quote;
    use syn::parse::{Parse, Parser};
    use syn::Token;

    // Parse syn::Type as a TokenStream, surrounded by angle brackets.
    fn example(input: ParseStream) -> Result<TokenStream> {
        let _langle: Token![<] = input.parse()?;
        let ty = recognize_token_stream(syn::Type::parse)(input)?;
        let _rangle: Token![>] = input.parse()?;
        Ok(ty)
    }

    let tokens = quote! { <fn() -> u8> };
    println!("{}", example.parse2(tokens).unwrap());
}
```

</div>

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-AnyDelimiter-for-ParseBuffer%3C'a%3E"
class="section impl">

<a href="../../src/syn/discouraged.rs.html#211-225"
class="src rightside">Source</a><a href="#impl-AnyDelimiter-for-ParseBuffer%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a href="discouraged/trait.AnyDelimiter.html" class="trait"
title="trait syn::parse::discouraged::AnyDelimiter">AnyDelimiter</a> for <a href="struct.ParseBuffer.html" class="struct"
title="struct syn::parse::ParseBuffer">ParseBuffer</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.parse_any_delimiter" class="section method trait-impl">

<a href="../../src/syn/discouraged.rs.html#212-224"
class="src rightside">Source</a><a href="#method.parse_any_delimiter" class="anchor">§</a>

#### fn <a
href="discouraged/trait.AnyDelimiter.html#tymethod.parse_any_delimiter"
class="fn">parse_any_delimiter</a>(&self) -\> <a href="../type.Result.html" class="type"
title="type syn::Result">Result</a>\<(<a href="../../proc_macro2/enum.Delimiter.html" class="enum"
title="enum proc_macro2::Delimiter">Delimiter</a>, <a href="../../proc_macro2/extra/struct.DelimSpan.html" class="struct"
title="struct proc_macro2::extra::DelimSpan">DelimSpan</a>, <a href="struct.ParseBuffer.html" class="struct"
title="struct syn::parse::ParseBuffer">ParseBuffer</a>\<'\_\>)\>

</div>

<div class="docblock">

Returns the delimiter, the span of the delimiter token, and the nested
contents for further parsing.

</div>

</div>

<div id="impl-Debug-for-ParseBuffer%3C'a%3E" class="section impl">

<a href="../../src/syn/parse.rs.html#283-287"
class="src rightside">Source</a><a href="#impl-Debug-for-ParseBuffer%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.ParseBuffer.html" class="struct"
title="struct syn::parse::ParseBuffer">ParseBuffer</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.fmt-1" class="section method trait-impl">

<a href="../../src/syn/parse.rs.html#284-286"
class="src rightside">Source</a><a href="#method.fmt-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt"
class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

<div class="docblock">

Formats the value using the given formatter. [Read
more](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt)

</div>

</div>

<div id="impl-Display-for-ParseBuffer%3C'a%3E" class="section impl">

<a href="../../src/syn/parse.rs.html#277-281"
class="src rightside">Source</a><a href="#impl-Display-for-ParseBuffer%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html"
class="trait" title="trait core::fmt::Display">Display</a> for <a href="struct.ParseBuffer.html" class="struct"
title="struct syn::parse::ParseBuffer">ParseBuffer</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../../src/syn/parse.rs.html#278-280"
class="src rightside">Source</a><a href="#method.fmt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html#tymethod.fmt"
class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

<div class="docblock">

Formats the value using the given formatter. [Read
more](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html#tymethod.fmt)

</div>

</div>

<div id="impl-Drop-for-ParseBuffer%3C'a%3E" class="section impl">

<a href="../../src/syn/parse.rs.html#265-275"
class="src rightside">Source</a><a href="#impl-Drop-for-ParseBuffer%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/ops/drop/trait.Drop.html"
class="trait" title="trait core::ops::drop::Drop">Drop</a> for <a href="struct.ParseBuffer.html" class="struct"
title="struct syn::parse::ParseBuffer">ParseBuffer</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.drop" class="section method trait-impl">

<a href="../../src/syn/parse.rs.html#266-274"
class="src rightside">Source</a><a href="#method.drop" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/drop/trait.Drop.html#tymethod.drop"
class="fn">drop</a>(&mut self)

</div>

<div class="docblock">

Executes the destructor for this type. [Read
more](https://doc.rust-lang.org/1.92.0/core/ops/drop/trait.Drop.html#tymethod.drop)

</div>

</div>

<div id="impl-Speculative-for-ParseBuffer%3C'a%3E" class="section impl">

<a href="../../src/syn/discouraged.rs.html#167-201"
class="src rightside">Source</a><a href="#impl-Speculative-for-ParseBuffer%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a href="discouraged/trait.Speculative.html" class="trait"
title="trait syn::parse::discouraged::Speculative">Speculative</a> for <a href="struct.ParseBuffer.html" class="struct"
title="struct syn::parse::ParseBuffer">ParseBuffer</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.advance_to" class="section method trait-impl">

<a href="../../src/syn/discouraged.rs.html#168-200"
class="src rightside">Source</a><a href="#method.advance_to" class="anchor">§</a>

#### fn <a href="discouraged/trait.Speculative.html#tymethod.advance_to"
class="fn">advance_to</a>(&self, fork: &Self)

</div>

<div class="docblock">

Advance this parse stream to the position of a forked parse stream.
[Read more](discouraged/trait.Speculative.html#tymethod.advance_to)

</div>

</div>

<div id="impl-RefUnwindSafe-for-ParseBuffer%3C'a%3E"
class="section impl">

<a href="../../src/syn/parse.rs.html#290"
class="src rightside">Source</a><a href="#impl-RefUnwindSafe-for-ParseBuffer%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.ParseBuffer.html" class="struct"
title="struct syn::parse::ParseBuffer">ParseBuffer</a>\<'a\>

</div>

<div id="impl-UnwindSafe-for-ParseBuffer%3C'a%3E" class="section impl">

<a href="../../src/syn/parse.rs.html#289"
class="src rightside">Source</a><a href="#impl-UnwindSafe-for-ParseBuffer%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.ParseBuffer.html" class="struct"
title="struct syn::parse::ParseBuffer">ParseBuffer</a>\<'a\>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-ParseBuffer%3C'a%3E" class="section impl">

<a href="#impl-Freeze-for-ParseBuffer%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.ParseBuffer.html" class="struct"
title="struct syn::parse::ParseBuffer">ParseBuffer</a>\<'a\>

</div>

<div id="impl-Send-for-ParseBuffer%3C'a%3E" class="section impl">

<a href="#impl-Send-for-ParseBuffer%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.ParseBuffer.html" class="struct"
title="struct syn::parse::ParseBuffer">ParseBuffer</a>\<'a\>

</div>

<div id="impl-Sync-for-ParseBuffer%3C'a%3E" class="section impl">

<a href="#impl-Sync-for-ParseBuffer%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.ParseBuffer.html" class="struct"
title="struct syn::parse::ParseBuffer">ParseBuffer</a>\<'a\>

</div>

<div id="impl-Unpin-for-ParseBuffer%3C'a%3E" class="section impl">

<a href="#impl-Unpin-for-ParseBuffer%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.ParseBuffer.html" class="struct"
title="struct syn::parse::ParseBuffer">ParseBuffer</a>\<'a\>

</div>

</div>

## Blanket Implementations<a href="#blanket-implementations" class="anchor">§</a>

<div id="blanket-implementations-list">

<div id="impl-Any-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/any.rs.html#138"
class="src rightside">Source</a><a href="#impl-Any-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html"
class="trait" title="trait core::any::Any">Any</a> for T

<div class="where">

where T: 'static +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.type_id" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/any.rs.html#139"
class="src rightside">Source</a><a href="#method.type_id" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html#tymethod.type_id"
class="fn">type_id</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/any/struct.TypeId.html"
class="struct" title="struct core::any::TypeId">TypeId</a>

</div>

<div class="docblock">

Gets the `TypeId` of `self`. [Read
more](https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html#tymethod.type_id)

</div>

</div>

<div id="impl-Borrow%3CT%3E-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#212"
class="src rightside">Source</a><a href="#impl-Borrow%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<T\> for T

<div class="where">

where T:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.borrow" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#214"
class="src rightside">Source</a><a href="#method.borrow" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html#tymethod.borrow"
class="fn">borrow</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>

</div>

<div class="docblock">

Immutably borrows from an owned value. [Read
more](https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html#tymethod.borrow)

</div>

</div>

<div id="impl-BorrowMut%3CT%3E-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#221"
class="src rightside">Source</a><a href="#impl-BorrowMut%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html"
class="trait" title="trait core::borrow::BorrowMut">BorrowMut</a>\<T\> for T

<div class="where">

where T:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.borrow_mut" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#222"
class="src rightside">Source</a><a href="#method.borrow_mut" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html#tymethod.borrow_mut"
class="fn">borrow_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>

</div>

<div class="docblock">

Mutably borrows from an owned value. [Read
more](https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html#tymethod.borrow_mut)

</div>

</div>

<div id="impl-From%3CT%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#785"
class="src rightside">Source</a><a href="#impl-From%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\> for T

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#788"
class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(t: T) -\> T

</div>

<div class="docblock">

Returns the argument unchanged.

</div>

</div>

<div id="impl-Into%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#767-769"
class="src rightside">Source</a><a href="#impl-Into%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<U\> for T

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="method.into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#777"
class="src rightside">Source</a><a href="#method.into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html#tymethod.into"
class="fn">into</a>(self) -\> U

</div>

<div class="docblock">

Calls `U::from(self)`.

That is, this conversion is whatever the implementation of
[`From`](https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html "trait core::convert::From")`<T> for U`
chooses to do.

</div>

</div>

<div id="impl-ToString-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/string.rs.html#2866"
class="src rightside">Source</a><a href="#impl-ToString-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/trait.ToString.html"
class="trait" title="trait alloc::string::ToString">ToString</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html"
class="trait" title="trait core::fmt::Display">Display</a> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.to_string" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/string.rs.html#2868"
class="src rightside">Source</a><a href="#method.to_string" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/trait.ToString.html#tymethod.to_string"
class="fn">to_string</a>(&self) -\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

</div>

<div class="docblock">

Converts the given value to a `String`. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/string/trait.ToString.html#tymethod.to_string)

</div>

</div>

<div id="impl-TryFrom%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#827-829"
class="src rightside">Source</a><a href="#impl-TryFrom%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<U\> for T

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Error-1"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#831"
class="src rightside">Source</a><a href="#associatedtype.Error-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype">Error</a> = <a
href="https://doc.rust-lang.org/1.92.0/core/convert/enum.Infallible.html"
class="enum" title="enum core::convert::Infallible">Infallible</a>

</div>

<div class="docblock">

The type returned in the event of a conversion error.

</div>

<div id="method.try_from" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#834"
class="src rightside">Source</a><a href="#method.try_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#tymethod.try_from"
class="fn">try_from</a>(value: U) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<T, \<T as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<U\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>\>

</div>

<div class="docblock">

Performs the conversion.

</div>

</div>

<div id="impl-TryInto%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#811-813"
class="src rightside">Source</a><a href="#impl-TryInto%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html"
class="trait" title="trait core::convert::TryInto">TryInto</a>\<U\> for T

<div class="where">

where U: <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Error"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#815"
class="src rightside">Source</a><a href="#associatedtype.Error" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html#associatedtype.Error"
class="associatedtype">Error</a> = \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>

</div>

<div class="docblock">

The type returned in the event of a conversion error.

</div>

<div id="method.try_into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#818"
class="src rightside">Source</a><a href="#method.try_into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html#tymethod.try_into"
class="fn">try_into</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<U, \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>\>

</div>

<div class="docblock">

Performs the conversion.

</div>

</div>

</div>

</div>

</div>
