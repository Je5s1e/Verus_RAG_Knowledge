<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](index.html)

</div>

# Macro <span class="macro">custom_keyword</span> Copy item path

<span class="sub-heading"><a href="../src/verus_syn/custom_keyword.rs.html#90-123"
class="src">Source</a> </span>

</div>

``` rust
macro_rules! custom_keyword {
    ($ident:ident) => { ... };
}
```

Expand description

<div class="docblock">

Define a type that supports parsing and printing a given identifier as
if it were a keyword.

## <a href="#usage" class="doc-anchor">§</a>Usage

As a convention, it is recommended that this macro be invoked within a
module called `kw` or `keyword` and that the resulting parser be invoked
with a `kw::` or `keyword::` prefix.

<div class="example-wrap">

``` rust
mod kw {
    syn::custom_keyword!(whatever);
}
```

</div>

The generated syntax tree node supports the following operations just
like any built-in keyword token.

- [Peeking](parse/struct.ParseBuffer.html#method.peek "method verus_syn::parse::ParseBuffer::peek")
  — `input.peek(kw::whatever)`

- [Parsing](parse/struct.ParseBuffer.html#method.parse "method verus_syn::parse::ParseBuffer::parse")
  — `input.parse::<kw::whatever>()?`

- [Printing](../quote/to_tokens/trait.ToTokens.html "trait quote::to_tokens::ToTokens")
  — `quote!( ... #whatever_token ... )`

- Construction from a
  [`Span`](../proc_macro2/struct.Span.html "struct proc_macro2::Span") —
  `let whatever_token = kw::whatever(sp)`

- Field access to its span — `let sp = whatever_token.span`

## <a href="#example" class="doc-anchor">§</a>Example

This example parses input that looks like `bool = true` or
`str = "value"`. The key must be either the identifier `bool` or the
identifier `str`. If `bool`, the value may be either `true` or `false`.
If `str`, the value may be any string literal.

The symbols `bool` and `str` are not reserved keywords in Rust so these
are not considered keywords in the `syn::token` module. Like any other
identifier that is not a keyword, these can be declared as custom
keywords by crates that need to use them as such.

<div class="example-wrap">

``` rust
use syn::{LitBool, LitStr, Result, Token};
use syn::parse::{Parse, ParseStream};

mod kw {
    syn::custom_keyword!(bool);
    syn::custom_keyword!(str);
}

enum Argument {
    Bool {
        bool_token: kw::bool,
        eq_token: Token![=],
        value: LitBool,
    },
    Str {
        str_token: kw::str,
        eq_token: Token![=],
        value: LitStr,
    },
}

impl Parse for Argument {
    fn parse(input: ParseStream) -> Result<Self> {
        let lookahead = input.lookahead1();
        if lookahead.peek(kw::bool) {
            Ok(Argument::Bool {
                bool_token: input.parse::<kw::bool>()?,
                eq_token: input.parse()?,
                value: input.parse()?,
            })
        } else if lookahead.peek(kw::str) {
            Ok(Argument::Str {
                str_token: input.parse::<kw::str>()?,
                eq_token: input.parse()?,
                value: input.parse()?,
            })
        } else {
            Err(lookahead.error())
        }
    }
}
```

</div>

</div>

</div>

</div>
