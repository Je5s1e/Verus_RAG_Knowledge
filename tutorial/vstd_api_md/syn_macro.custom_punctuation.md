<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](index.html)

</div>

# Macro <span class="macro">custom_punctuation</span> Copy item path

<span class="sub-heading"><a href="../src/syn/custom_punctuation.rs.html#79-110"
class="src">Source</a> </span>

</div>

``` rust
macro_rules! custom_punctuation {
    ($ident:ident, $($tt:tt)+) => { ... };
}
```

Expand description

<div class="docblock">

Define a type that supports parsing and printing a multi-character
symbol as if it were a punctuation token.

## <a href="#usage" class="doc-anchor">§</a>Usage

<div class="example-wrap">

``` rust
syn::custom_punctuation!(LeftRightArrow, <=>);
```

</div>

The generated syntax tree node supports the following operations just
like any built-in punctuation token.

- [Peeking](parse/struct.ParseBuffer.html#method.peek "method syn::parse::ParseBuffer::peek")
  — `input.peek(LeftRightArrow)`

- [Parsing](parse/struct.ParseBuffer.html#method.parse "method syn::parse::ParseBuffer::parse")
  — `input.parse::<LeftRightArrow>()?`

- [Printing](../quote/to_tokens/trait.ToTokens.html "trait quote::to_tokens::ToTokens")
  — `quote!( ... #lrarrow ... )`

- Construction from a
  [`Span`](../proc_macro2/struct.Span.html "struct proc_macro2::Span") —
  `let lrarrow = LeftRightArrow(sp)`

- Construction from multiple
  [`Span`](../proc_macro2/struct.Span.html "struct proc_macro2::Span") —
  `let lrarrow = LeftRightArrow([sp, sp, sp])`

- Field access to its spans — `let spans = lrarrow.spans`

## <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use core::iter;
use proc_macro2::{TokenStream, TokenTree};
use syn::parse::{Parse, ParseStream, Peek, Result};
use syn::punctuated::Punctuated;
use syn::Expr;

syn::custom_punctuation!(PathSeparator, </>);

// expr </> expr </> expr ...
struct PathSegments {
    segments: Punctuated<Expr, PathSeparator>,
}

impl Parse for PathSegments {
    fn parse(input: ParseStream) -> Result<Self> {
        let mut segments = Punctuated::new();

        let first = parse_until(input, PathSeparator)?;
        segments.push_value(syn::parse2(first)?);

        while input.peek(PathSeparator) {
            segments.push_punct(input.parse()?);

            let next = parse_until(input, PathSeparator)?;
            segments.push_value(syn::parse2(next)?);
        }

        Ok(PathSegments { segments })
    }
}

fn parse_until<E: Peek>(input: ParseStream, end: E) -> Result<TokenStream> {
    let mut tokens = TokenStream::new();
    while !input.is_empty() && !input.peek(end) {
        let next: TokenTree = input.parse()?;
        tokens.extend(iter::once(next));
    }
    Ok(tokens)
}

fn main() {
    let input = r#" a::b </> c::d::e "#;
    let _: PathSegments = syn::parse_str(input).unwrap();
}
```

</div>

</div>

</div>

</div>
