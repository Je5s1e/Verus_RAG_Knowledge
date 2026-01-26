<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)::[meta](index.html)

</div>

# Function <span class="fn">parser</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/meta.rs.html#132-140"
class="src">Source</a> </span>

</div>

``` rust
pub fn parser(
    logic: impl FnMut(ParseNestedMeta<'_>) -> Result<()>,
) -> impl Parser<Output = ()>
```

Expand description

<div class="docblock">

Make a parser that is usable with `parse_macro_input!` in a
`#[proc_macro_attribute]` macro.

*Warning:* When parsing attribute args **other than** the
`proc_macro::TokenStream` input of a `proc_macro_attribute`, you do
**not** need this function. In several cases your callers will get worse
error messages if you use this function, because the surrounding
delimiter’s span is concealed from attribute macros by rustc. Use
[`Attribute::parse_nested_meta`](../struct.Attribute.html#method.parse_nested_meta "method verus_syn::Attribute::parse_nested_meta")
instead.

## <a href="#example" class="doc-anchor">§</a>Example

This example implements an attribute macro whose invocations look like
this:

<div class="example-wrap">

``` rust
#[tea(kind = "EarlGrey", hot)]
struct Picard {...}
```

</div>

The “parameters” supported by the attribute are:

- `kind = "..."`
- `hot`
- `with(sugar, milk, ...)`, a comma-separated list of ingredients

<div class="example-wrap">

``` rust
use proc_macro::TokenStream;
use syn::{parse_macro_input, LitStr, Path};

#[proc_macro_attribute]
pub fn tea(args: TokenStream, input: TokenStream) -> TokenStream {
    let mut kind: Option<LitStr> = None;
    let mut hot: bool = false;
    let mut with: Vec<Path> = Vec::new();
    let tea_parser = syn::meta::parser(|meta| {
        if meta.path.is_ident("kind") {
            kind = Some(meta.value()?.parse()?);
            Ok(())
        } else if meta.path.is_ident("hot") {
            hot = true;
            Ok(())
        } else if meta.path.is_ident("with") {
            meta.parse_nested_meta(|meta| {
                with.push(meta.path);
                Ok(())
            })
        } else {
            Err(meta.error("unsupported tea property"))
        }
    });

    parse_macro_input!(args with tea_parser);
    eprintln!("kind={kind:?} hot={hot} with={with:?}");

    /* ... */
}
```

</div>

The `syn::meta` library will take care of dealing with the commas
including trailing commas, and producing sensible error messages on
unexpected input.

<div class="example-wrap">

``` console
error: expected `,`
 --> src/main.rs:3:37
  |
3 | #[tea(kind = "EarlGrey", with(sugar = "lol", milk))]
  |                                     ^
```

</div>

## <a href="#example-1" class="doc-anchor">§</a>Example

Same as above but we factor out most of the logic into a separate
function.

<div class="example-wrap">

``` rust
use proc_macro::TokenStream;
use syn::meta::ParseNestedMeta;
use syn::parse::{Parser, Result};
use syn::{parse_macro_input, LitStr, Path};

#[proc_macro_attribute]
pub fn tea(args: TokenStream, input: TokenStream) -> TokenStream {
    let mut attrs = TeaAttributes::default();
    let tea_parser = syn::meta::parser(|meta| attrs.parse(meta));
    parse_macro_input!(args with tea_parser);

    /* ... */
}

#[derive(Default)]
struct TeaAttributes {
    kind: Option<LitStr>,
    hot: bool,
    with: Vec<Path>,
}

impl TeaAttributes {
    fn parse(&mut self, meta: ParseNestedMeta) -> Result<()> {
        if meta.path.is_ident("kind") {
            self.kind = Some(meta.value()?.parse()?);
            Ok(())
        } else /* just like in last example */

    }
}
```

</div>

</div>

</div>

</div>
