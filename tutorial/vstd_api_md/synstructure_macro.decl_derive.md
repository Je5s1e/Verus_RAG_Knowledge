<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[synstructure](index.html)

</div>

# Macro <span class="macro">decl_derive</span> Copy item path

<span class="sub-heading"><a href="../src/synstructure/macros.rs.html#89-113"
class="src">Source</a> </span>

</div>

``` rust
macro_rules! decl_derive {
    ([$derives:ident $($derive_t:tt)*] => $(#[$($attrs:tt)*])* $inner:path) => { ... };
}
```

Expand description

<div class="docblock">

The `decl_derive!` macro declares a custom derive wrapper. It will parse
the incoming `TokenStream` into a `synstructure::Structure` object, and
pass it into the inner function.

Your inner function should take a `synstructure::Structure` by value,
and return a type implementing `synstructure::MacroResult`, for example:

<div class="example-wrap">

``` rust
fn derive_simple(input: synstructure::Structure) -> proc_macro2::TokenStream {
    unimplemented!()
}

fn derive_result(input: synstructure::Structure)
    -> syn::Result<proc_macro2::TokenStream>
{
    unimplemented!()
}
```

</div>

## <a href="#usage" class="doc-anchor">§</a>Usage

#### <a href="#without-attributes" class="doc-anchor">§</a>Without Attributes

<div class="example-wrap">

``` rust
fn derive_interesting(_input: synstructure::Structure) -> proc_macro2::TokenStream {
    quote::quote! { ... }
}

decl_derive!([Interesting] => derive_interesting);
```

</div>

#### <a href="#with-attributes" class="doc-anchor">§</a>With Attributes

<div class="example-wrap">

``` rust
fn derive_interesting(_input: synstructure::Structure) -> proc_macro2::TokenStream {
    quote::quote! { ... }
}

decl_derive!([Interesting, attributes(interesting_ignore)] => derive_interesting);
```

</div>

#### <a href="#decl-attributes--doc-comments" class="doc-anchor">§</a>Decl Attributes & Doc Comments

<div class="example-wrap">

``` rust
fn derive_interesting(_input: synstructure::Structure) -> proc_macro2::TokenStream {
    quote::quote! { ... }
}

decl_derive! {
    [Interesting] =>
    #[allow(some_lint)]
    /// Documentation Comments
    derive_interesting
}
```

</div>

*This macro is available if `synstructure` is built with the
`"proc-macro"` feature.*

</div>

</div>

</div>
