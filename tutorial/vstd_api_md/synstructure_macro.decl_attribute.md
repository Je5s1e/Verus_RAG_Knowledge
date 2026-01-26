<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[synstructure](index.html)

</div>

# Macro <span class="macro">decl_attribute</span> Copy item path

<span class="sub-heading"><a href="../src/synstructure/macros.rs.html#152-177"
class="src">Source</a> </span>

</div>

``` rust
macro_rules! decl_attribute {
    ([$attribute:ident] => $(#[$($attrs:tt)*])* $inner:path) => { ... };
}
```

Expand description

<div class="docblock">

The `decl_attribute!` macro declares a custom attribute wrapper. It will
parse the incoming `TokenStream` into a `synstructure::Structure`
object, and pass it into the inner function.

Your inner function should have the following type:

<div class="example-wrap">

``` rust
fn attribute(
    attr: proc_macro2::TokenStream,
    structure: synstructure::Structure,
) -> proc_macro2::TokenStream {
    unimplemented!()
}
```

</div>

## <a href="#usage" class="doc-anchor">§</a>Usage

<div class="example-wrap">

``` rust
fn attribute_interesting(
    _attr: proc_macro2::TokenStream,
    _structure: synstructure::Structure,
) -> proc_macro2::TokenStream {
    quote::quote! { ... }
}

decl_attribute!([interesting] => attribute_interesting);
```

</div>

*This macro is available if `synstructure` is built with the
`"proc-macro"` feature.*

</div>

</div>

</div>
