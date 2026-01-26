<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](../index.html)

</div>

# Module spanned Copy item path

<span class="sub-heading"><a href="../../src/syn/spanned.rs.html#1-118" class="src">Source</a>
</span>

</div>

Expand description

<div class="docblock">

A trait that can provide the `Span` of the complete contents of a syntax
tree node.

  

## <a href="#example" class="doc-anchor">§</a>Example

Suppose in a procedural macro we have a
[`Type`](../enum.Type.html "enum syn::Type") that we want to assert
implements the
[`Sync`](https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html "trait core::marker::Sync")
trait. Maybe this is the type of one of the fields of a struct for which
we are deriving a trait implementation, and we need to be able to pass a
reference to one of those fields across threads.

If the field type does *not* implement `Sync` as required, we want the
compiler to report an error pointing out exactly which type it was.

The following macro code takes a variable `ty` of type `Type` and
produces a static assertion that `Sync` is implemented for that type.

<div class="example-wrap">

``` rust
use proc_macro::TokenStream;
use proc_macro2::Span;
use quote::quote_spanned;
use syn::Type;
use syn::spanned::Spanned;

#[proc_macro_derive(MyMacro)]
pub fn my_macro(input: TokenStream) -> TokenStream {
    /* ... */

    let assert_sync = quote_spanned! {ty.span()=>
        struct _AssertSync where #ty: Sync;
    };

    /* ... */
}
```

</div>

By inserting this `assert_sync` fragment into the output code generated
by our macro, the user’s code will fail to compile if `ty` does not
implement `Sync`. The errors they would see look like the following.

<div class="example-wrap">

``` text
error[E0277]: the trait bound `*const i32: core::marker::Sync` is not satisfied
  --> src/main.rs:10:21
   |
10 |     bad_field: *const i32,
   |                ^^^^^^^^^^ `*const i32` cannot be shared between threads safely
```

</div>

In this technique, using the `Type`’s span for the error message makes
the error appear in the correct place underlining the right type.

  

## <a href="#limitations" class="doc-anchor">§</a>Limitations

The underlying
[`proc_macro::Span::join`](https://doc.rust-lang.org/1.92.0/proc_macro/struct.Span.html#method.join "method proc_macro::Span::join")
method is nightly-only. When called from within a procedural macro in a
nightly compiler, `Spanned` will use `join` to produce the intended
span. When not using a nightly compiler, only the span of the *first
token* of the syntax tree node is returned.

In the common case of wanting to use the joined span as the span of a
`syn::Error`, consider instead using
[`syn::Error::new_spanned`](../struct.Error.html#method.new_spanned "associated function syn::Error::new_spanned")
which is able to span the error correctly under the complete syntax tree
node without needing the unstable `join`.

</div>

## Traits<a href="#traits" class="anchor">§</a>

<a href="trait.Spanned.html" class="trait"
title="trait syn::spanned::Spanned">Spanned</a>  
A trait that can provide the `Span` of the complete contents of a syntax
tree node.

</div>

</div>
