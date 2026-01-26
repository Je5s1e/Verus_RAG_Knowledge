<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](index.html)

</div>

# Macro <span class="macro">parse_quote</span> Copy item path

<span class="sub-heading"><a href="../src/verus_syn/parse_quote.rs.html#80-84"
class="src">Source</a> </span>

</div>

``` rust
macro_rules! parse_quote {
    ($($tt:tt)*) => { ... };
}
```

Expand description

<div class="docblock">

Quasi-quotation macro that accepts input like the
[`quote!`](https://docs.rs/quote/1.0/quote/index.html) macro but uses
type inference to figure out a return type for those tokens.

The return type can be any syntax tree node that implements the
[`Parse`](parse/trait.Parse.html "trait verus_syn::parse::Parse") trait.

<div class="example-wrap">

``` rust
use quote::quote;
use syn::{parse_quote, Stmt};

fn main() {
    let name = quote!(v);
    let ty = quote!(u8);

    let stmt: Stmt = parse_quote! {
        let #name: #ty = Default::default();
    };

    println!("{:#?}", stmt);
}
```

</div>

*This macro is available only if Syn is built with both the `"parsing"`
and `"printing"` features.*

## <a href="#example" class="doc-anchor">§</a>Example

The following helper function adds a bound `T: HeapSize` to every type
parameter `T` in the input generics.

<div class="example-wrap">

``` rust
use syn::{parse_quote, Generics, GenericParam};

// Add a bound `T: HeapSize` to every type parameter T.
fn add_trait_bounds(mut generics: Generics) -> Generics {
    for param in &mut generics.params {
        if let GenericParam::Type(type_param) = param {
            type_param.bounds.push(parse_quote!(HeapSize));
        }
    }
    generics
}
```

</div>

## <a href="#special-cases" class="doc-anchor">§</a>Special cases

This macro can parse the following additional types as a special case
even though they do not implement the `Parse` trait.

- [`Attribute`](struct.Attribute.html "struct verus_syn::Attribute") —
  parses one attribute, allowing either outer like `#[...]` or inner
  like `#![...]`
- [`Vec<Attribute>`](struct.Attribute.html "struct verus_syn::Attribute")
  — parses multiple attributes, including mixed kinds in any order
- [`Punctuated<T, P>`](punctuated/struct.Punctuated.html "struct verus_syn::punctuated::Punctuated")
  — parses zero or more `T` separated by punctuation `P` with optional
  trailing punctuation
- [`Vec<Arm>`](struct.Arm.html "struct verus_syn::Arm") — parses arms
  separated by optional commas according to the same grammar as the
  inside of a `match` expression
- [`Vec<Stmt>`](struct.Block.html#method.parse_within "associated function verus_syn::Block::parse_within")
  — parses the same as `Block::parse_within`
- [`Pat`](enum.Pat.html#method.parse_multi_with_leading_vert "associated function verus_syn::Pat::parse_multi_with_leading_vert"),
  [`Box<Pat>`](enum.Pat.html#method.parse_multi_with_leading_vert "associated function verus_syn::Pat::parse_multi_with_leading_vert")
  — parses the same as `Pat::parse_multi_with_leading_vert`
- [`Field`](struct.Field.html "struct verus_syn::Field") — parses a
  named or unnamed struct field

## <a href="#panics" class="doc-anchor">§</a>Panics

Panics if the tokens fail to parse as the expected syntax tree type. The
caller is responsible for ensuring that the input tokens are
syntactically valid.

</div>

</div>

</div>
