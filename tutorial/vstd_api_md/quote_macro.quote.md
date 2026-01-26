<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[quote](index.html)

</div>

# Macro <span class="macro">quote</span> Copy item path

<span class="sub-heading"><a href="../src/quote/lib.rs.html#484-488" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! quote {
    ($($tt:tt)*) => { ... };
}
```

Expand description

<div class="docblock">

The whole point.

Performs variable interpolation against the input and produces it as
[`proc_macro2::TokenStream`](../proc_macro2/struct.TokenStream.html "struct proc_macro2::TokenStream").

Note: for returning tokens to the compiler in a procedural macro, use
`.into()` on the result to convert to
[`proc_macro::TokenStream`](https://doc.rust-lang.org/1.92.0/proc_macro/struct.TokenStream.html "struct proc_macro::TokenStream").

  

## <a href="#interpolation" class="doc-anchor">§</a>Interpolation

Variable interpolation is done with `#var` (similar to `$var` in
`macro_rules!` macros). This grabs the `var` variable that is currently
in scope and inserts it in that location in the output tokens. Any type
implementing the
[`ToTokens`](trait.ToTokens.html "trait quote::ToTokens") trait can be
interpolated. This includes most Rust primitive types as well as most of
the syntax tree types from the [Syn](https://github.com/dtolnay/syn)
crate.

Repetition is done using `#(...)*` or `#(...),*` again similar to
`macro_rules!`. This iterates through the elements of any variable
interpolated within the repetition and inserts a copy of the repetition
body for each one. The variables in an interpolation may be a `Vec`,
slice, `BTreeSet`, or any `Iterator`.

- `#(#var)*` — no separators
- `#(#var),*` — the character before the asterisk is used as a separator
- `#( struct #var; )*` — the repetition can contain other tokens
- `#( #k => println!("{}", #v), )*` — even multiple interpolations

  

## <a href="#hygiene" class="doc-anchor">§</a>Hygiene

Any interpolated tokens preserve the `Span` information provided by
their `ToTokens` implementation. Tokens that originate within the
`quote!` invocation are spanned with
[`Span::call_site()`](../proc_macro2/struct.Span.html#method.call_site "associated function proc_macro2::Span::call_site").

A different span can be provided through the
[`quote_spanned!`](macro.quote_spanned.html "macro quote::quote_spanned")
macro.

  

## <a href="#return-type" class="doc-anchor">§</a>Return type

The macro evaluates to an expression of type `proc_macro2::TokenStream`.
Meanwhile Rust procedural macros are expected to return the type
`proc_macro::TokenStream`.

The difference between the two types is that `proc_macro` types are
entirely specific to procedural macros and cannot ever exist in code
outside of a procedural macro, while `proc_macro2` types may exist
anywhere including tests and non-macro code like main.rs and build.rs.
This is why even the procedural macro ecosystem is largely built around
`proc_macro2`, because that ensures the libraries are unit testable and
accessible in non-macro contexts.

There is a
[`From`](https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html "trait core::convert::From")-conversion
in both directions so returning the output of `quote!` from a procedural
macro usually looks like `tokens.into()` or
`proc_macro::TokenStream::from(tokens)`.

  

## <a href="#examples" class="doc-anchor">§</a>Examples

#### <a href="#procedural-macro" class="doc-anchor">§</a>Procedural macro

The structure of a basic procedural macro is as follows. Refer to the
[Syn](https://github.com/dtolnay/syn) crate for further useful guidance
on using `quote!` as part of a procedural macro.

<div class="example-wrap">

``` rust
extern crate proc_macro;

use proc_macro::TokenStream;
use quote::quote;

#[proc_macro_derive(HeapSize)]
pub fn derive_heap_size(input: TokenStream) -> TokenStream {
    // Parse the input and figure out what implementation to generate...
    let name = /* ... */;
    let expr = /* ... */;

    let expanded = quote! {
        // The generated impl.
        impl heapsize::HeapSize for #name {
            fn heap_size_of_children(&self) -> usize {
                #expr
            }
        }
    };

    // Hand the output tokens back to the compiler.
    TokenStream::from(expanded)
}
```

</div>

  

#### <a href="#combining-quoted-fragments" class="doc-anchor">§</a>Combining quoted fragments

Usually you don’t end up constructing an entire final `TokenStream` in
one piece. Different parts may come from different helper functions. The
tokens produced by `quote!` themselves implement `ToTokens` and so can
be interpolated into later `quote!` invocations to build up a final
result.

<div class="example-wrap">

``` rust
let type_definition = quote! {...};
let methods = quote! {...};

let tokens = quote! {
    #type_definition
    #methods
};
```

</div>

  

#### <a href="#constructing-identifiers" class="doc-anchor">§</a>Constructing identifiers

Suppose we have an identifier `ident` which came from somewhere in a
macro input and we need to modify it in some way for the macro output.
Let’s consider prepending the identifier with an underscore.

Simply interpolating the identifier next to an underscore will not have
the behavior of concatenating them. The underscore and the identifier
will continue to be two separate tokens as if you had written `_ x`.

<div class="example-wrap edition">

<a href="#" class="tooltip"
title="This example runs with edition 2018">ⓘ</a>

``` rust
// incorrect
quote! {
    let mut _#ident = 0;
}
```

</div>

The solution is to build a new identifier token with the correct value.
As this is such a common case, the
[`format_ident!`](macro.format_ident.html "macro quote::format_ident")
macro provides a convenient utility for doing so correctly.

<div class="example-wrap">

``` rust
let varname = format_ident!("_{}", ident);
quote! {
    let mut #varname = 0;
}
```

</div>

Alternatively, the APIs provided by Syn and proc-macro2 can be used to
directly build the identifier. This is roughly equivalent to the above,
but will not handle `ident` being a raw identifier.

<div class="example-wrap">

``` rust
let concatenated = format!("_{}", ident);
let varname = syn::Ident::new(&concatenated, ident.span());
quote! {
    let mut #varname = 0;
}
```

</div>

  

#### <a href="#making-method-calls" class="doc-anchor">§</a>Making method calls

Let’s say our macro requires some type specified in the macro input to
have a constructor called `new`. We have the type in a variable called
`field_type` of type `syn::Type` and want to invoke the constructor.

<div class="example-wrap">

``` rust
// incorrect
quote! {
    let value = #field_type::new();
}
```

</div>

This works only sometimes. If `field_type` is `String`, the expanded
code contains `String::new()` which is fine. But if `field_type` is
something like `Vec<i32>` then the expanded code is `Vec<i32>::new()`
which is invalid syntax. Ordinarily in handwritten Rust we would write
`Vec::<i32>::new()` but for macros often the following is more
convenient.

<div class="example-wrap">

``` rust
quote! {
    let value = <#field_type>::new();
}
```

</div>

This expands to `<Vec<i32>>::new()` which behaves correctly.

A similar pattern is appropriate for trait methods.

<div class="example-wrap">

``` rust
quote! {
    let value = <#field_type as core::default::Default>::default();
}
```

</div>

  

#### <a href="#interpolating-text-inside-of-doc-comments"
class="doc-anchor">§</a>Interpolating text inside of doc comments

Neither doc comments nor string literals get interpolation behavior in
quote:

<div class="example-wrap compile_fail">

<a href="#" class="tooltip"
title="This example deliberately fails to compile">ⓘ</a>

``` rust
quote! {
    /// try to interpolate: #ident
    ///
    /// ...
}
```

</div>

<div class="example-wrap compile_fail">

<a href="#" class="tooltip"
title="This example deliberately fails to compile">ⓘ</a>

``` rust
quote! {
    #[doc = "try to interpolate: #ident"]
}
```

</div>

Instead the best way to build doc comments that involve variables is by
formatting the doc string literal outside of quote.

<div class="example-wrap">

``` rust
let msg = format!(...);
quote! {
    #[doc = #msg]
    ///
    /// ...
}
```

</div>

  

#### <a href="#indexing-into-a-tuple-struct" class="doc-anchor">§</a>Indexing into a tuple struct

When interpolating indices of a tuple or tuple struct, we need them not
to appears suffixed as integer literals by interpolating them as
[`syn::Index`](https://docs.rs/syn/2.0/syn/struct.Index.html) instead.

<div class="example-wrap compile_fail">

<a href="#" class="tooltip"
title="This example deliberately fails to compile">ⓘ</a>

``` rust
let i = 0usize..self.fields.len();

// expands to 0 + self.0usize.heap_size() + self.1usize.heap_size() + ...
// which is not valid syntax
quote! {
    0 #( + self.#i.heap_size() )*
}
```

</div>

<div class="example-wrap">

``` rust
let i = (0..self.fields.len()).map(syn::Index::from);

// expands to 0 + self.0.heap_size() + self.1.heap_size() + ...
quote! {
    0 #( + self.#i.heap_size() )*
}
```

</div>

</div>

</div>

</div>
