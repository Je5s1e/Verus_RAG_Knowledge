<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[synstructure](index.html)

</div>

# Struct <span class="struct">Structure</span> Copy item path

<span class="sub-heading"><a href="../src/synstructure/lib.rs.html#996-1003"
class="src">Source</a> </span>

</div>

``` rust
pub struct Structure<'a> { /* private fields */ }
```

Expand description

<div class="docblock">

A wrapper around a `syn::DeriveInput` which provides utilities for
creating custom derive trait implementations.

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-Structure%3C'a%3E" class="section impl">

<a href="../src/synstructure/lib.rs.html#1005-2386"
class="src rightside">Source</a><a href="#impl-Structure%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="struct.Structure.html" class="struct"
title="struct synstructure::Structure">Structure</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.new" class="section method">

<a href="../src/synstructure/lib.rs.html#1013-1015"
class="src rightside">Source</a>

#### pub fn <a href="#method.new" class="fn">new</a>(ast: &'a <a href="../syn/derive/struct.DeriveInput.html" class="struct"
title="struct syn::derive::DeriveInput">DeriveInput</a>) -\> Self

</div>

<div class="docblock">

Create a new `Structure` with the variants and fields from the passed-in
`DeriveInput`.

##### <a href="#panics" class="doc-anchor">§</a>Panics

This method will panic if the provided AST node represents an untagged
union.

</div>

<div id="method.try_new" class="section method">

<a href="../src/synstructure/lib.rs.html#1022-1067"
class="src rightside">Source</a>

#### pub fn <a href="#method.try_new" class="fn">try_new</a>(ast: &'a <a href="../syn/derive/struct.DeriveInput.html" class="struct"
title="struct syn::derive::DeriveInput">DeriveInput</a>) -\> <a href="../syn/error/type.Result.html" class="type"
title="type syn::error::Result">Result</a>\<Self\>

</div>

<div class="docblock">

Create a new `Structure` with the variants and fields from the passed-in
`DeriveInput`.

Unlike `Structure::new`, this method does not panic if the provided AST
node represents an untagged union.

</div>

<div id="method.variants" class="section method">

<a href="../src/synstructure/lib.rs.html#1070-1072"
class="src rightside">Source</a>

#### pub fn <a href="#method.variants" class="fn">variants</a>(&self) -\> &\[<a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>\]

</div>

<div class="docblock">

Returns a slice of the variants in this Structure.

</div>

<div id="method.variants_mut" class="section method">

<a href="../src/synstructure/lib.rs.html#1075-1077"
class="src rightside">Source</a>

#### pub fn <a href="#method.variants_mut" class="fn">variants_mut</a>(&mut self) -\> &mut \[<a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>\]

</div>

<div class="docblock">

Returns a mut slice of the variants in this Structure.

</div>

<div id="method.ast" class="section method">

<a href="../src/synstructure/lib.rs.html#1081-1083"
class="src rightside">Source</a>

#### pub fn <a href="#method.ast" class="fn">ast</a>(&self) -\> &'a <a href="../syn/derive/struct.DeriveInput.html" class="struct"
title="struct syn::derive::DeriveInput">DeriveInput</a>

</div>

<div class="docblock">

Returns a reference to the underlying `syn` AST node which this
`Structure` was created from.

</div>

<div id="method.omitted_variants" class="section method">

<a href="../src/synstructure/lib.rs.html#1086-1088"
class="src rightside">Source</a>

#### pub fn <a href="#method.omitted_variants" class="fn">omitted_variants</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

True if any variants were omitted due to a `filter_variants` call.

</div>

<div id="method.each" class="section method">

<a href="../src/synstructure/lib.rs.html#1121-1134"
class="src rightside">Source</a>

#### pub fn <a href="#method.each" class="fn">each</a>\<F, R\>(&self, f: F) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&<a href="struct.BindingInfo.html" class="struct"
title="struct synstructure::BindingInfo">BindingInfo</a>\<'\_\>) -\> R,
R: <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>,

</div>

</div>

<div class="docblock">

Runs the passed-in function once for each bound field, passing in a
`BindingInfo`. and generating `match` arms which evaluate the returned
tokens.

This method will ignore variants or fields which are ignored through the
`filter` and `filter_variant` methods.

##### <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A {
        B(i32, i32),
        C(u32),
    }
};
let s = Structure::new(&di);

assert_eq!(
    s.each(|bi| quote!(println!("{:?}", #bi))).to_string(),

    quote!{
        A::B(ref __binding_0, ref __binding_1,) => {
            { println!("{:?}", __binding_0) }
            { println!("{:?}", __binding_1) }
        }
        A::C(ref __binding_0,) => {
            { println!("{:?}", __binding_0) }
        }
    }.to_string()
);
```

</div>

</div>

<div id="method.fold" class="section method">

<a href="../src/synstructure/lib.rs.html#1169-1183"
class="src rightside">Source</a>

#### pub fn <a href="#method.fold" class="fn">fold</a>\<F, I, R\>(&self, init: I, f: F) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>,
&<a href="struct.BindingInfo.html" class="struct"
title="struct synstructure::BindingInfo">BindingInfo</a>\<'\_\>) -\> R,
I: <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>, R:
<a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>,

</div>

</div>

<div class="docblock">

Runs the passed-in function once for each bound field, passing in the
result of the previous call, and a `BindingInfo`. generating `match`
arms which evaluate to the resulting tokens.

This method will ignore variants or fields which are ignored through the
`filter` and `filter_variant` methods.

If a variant has been ignored, it will return the `init` value.

##### <a href="#example-1" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A {
        B(i32, i32),
        C(u32),
    }
};
let s = Structure::new(&di);

assert_eq!(
    s.fold(quote!(0), |acc, bi| quote!(#acc + #bi)).to_string(),

    quote!{
        A::B(ref __binding_0, ref __binding_1,) => {
            0 + __binding_0 + __binding_1
        }
        A::C(ref __binding_0,) => {
            0 + __binding_0
        }
    }.to_string()
);
```

</div>

</div>

<div id="method.each_variant" class="section method">

<a href="../src/synstructure/lib.rs.html#1219-1234"
class="src rightside">Source</a>

#### pub fn <a href="#method.each_variant" class="fn">each_variant</a>\<F, R\>(&self, f: F) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&<a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'\_\>) -\> R,
R: <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>,

</div>

</div>

<div class="docblock">

Runs the passed-in function once for each variant, passing in a
`VariantInfo`. and generating `match` arms which evaluate the returned
tokens.

This method will ignore variants and not bind fields which are ignored
through the `filter` and `filter_variant` methods.

##### <a href="#example-2" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A {
        B(i32, i32),
        C(u32),
    }
};
let s = Structure::new(&di);

assert_eq!(
    s.each_variant(|v| {
        let name = &v.ast().ident;
        quote!(println!(stringify!(#name)))
    }).to_string(),

    quote!{
        A::B(ref __binding_0, ref __binding_1,) => {
            println!(stringify!(B))
        }
        A::C(ref __binding_0,) => {
            println!(stringify!(C))
        }
    }.to_string()
);
```

</div>

</div>

<div id="method.filter" class="section method">

<a href="../src/synstructure/lib.rs.html#1273-1281"
class="src rightside">Source</a>

#### pub fn <a href="#method.filter" class="fn">filter</a>\<F\>(&mut self, f: F) -\> &mut Self

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&<a href="struct.BindingInfo.html" class="struct"
title="struct synstructure::BindingInfo">BindingInfo</a>\<'\_\>) -\>
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Filter the bindings created by this `Structure` object. This has 2
effects:

- The bindings will no longer appear in match arms generated by methods
  on this `Structure` or its subobjects.

- Impl blocks created with the `bound_impl` or `unsafe_bound_impl`
  method only consider type parameters referenced in the types of
  non-filtered fields.

##### <a href="#example-3" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A {
        B{ a: i32, b: i32 },
        C{ a: u32 },
    }
};
let mut s = Structure::new(&di);

s.filter(|bi| {
    bi.ast().ident == Some(quote::format_ident!("a"))
});

assert_eq!(
    s.each(|bi| quote!(println!("{:?}", #bi))).to_string(),

    quote!{
        A::B{ a: ref __binding_0, .. } => {
            { println!("{:?}", __binding_0) }
        }
        A::C{ a: ref __binding_0, } => {
            { println!("{:?}", __binding_0) }
        }
    }.to_string()
);
```

</div>

</div>

<div id="method.drain_filter" class="section method">

<a href="../src/synstructure/lib.rs.html#1333-1349"
class="src rightside">Source</a>

#### pub fn <a href="#method.drain_filter" class="fn">drain_filter</a>\<F\>(&mut self, f: F) -\> Self

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&<a href="struct.BindingInfo.html" class="struct"
title="struct synstructure::BindingInfo">BindingInfo</a>\<'\_\>) -\>
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Iterates all the bindings of this `Structure` object and uses a closure
to determine if a binding should be removed. If the closure returns
`true` the binding is removed from the structure. If the closure returns
`false`, the binding remains in the structure.

All the removed bindings are moved to a new `Structure` object which is
otherwise identical to the current one. To understand the effects of
removing a binding from a structure check the
[`Structure::filter`](struct.Structure.html#method.filter "method synstructure::Structure::filter")
documentation.

##### <a href="#example-4" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A {
        B{ a: i32, b: i32 },
        C{ a: u32 },
    }
};
let mut with_b = Structure::new(&di);

let with_a = with_b.drain_filter(|bi| {
    bi.ast().ident == Some(quote::format_ident!("a"))
});

assert_eq!(
    with_a.each(|bi| quote!(println!("{:?}", #bi))).to_string(),

    quote!{
        A::B{ a: ref __binding_0, .. } => {
            { println!("{:?}", __binding_0) }
        }
        A::C{ a: ref __binding_0, } => {
            { println!("{:?}", __binding_0) }
        }
    }.to_string()
);

assert_eq!(
    with_b.each(|bi| quote!(println!("{:?}", #bi))).to_string(),

    quote!{
        A::B{ b: ref __binding_1, .. } => {
            { println!("{:?}", __binding_1) }
        }
        A::C{ .. } => {

        }
    }.to_string()
);
```

</div>

</div>

<div id="method.add_where_predicate" class="section method">

<a href="../src/synstructure/lib.rs.html#1388-1391"
class="src rightside">Source</a>

#### pub fn <a href="#method.add_where_predicate" class="fn">add_where_predicate</a>(&mut self, pred: <a href="../syn/generics/enum.WherePredicate.html" class="enum"
title="enum syn::generics::WherePredicate">WherePredicate</a>) -\> &mut Self

</div>

<div class="docblock">

Specify additional where predicate bounds which should be generated by
impl-generating functions such as `gen_impl`, `bound_impl`, and
`unsafe_bound_impl`.

##### <a href="#example-5" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A<T, U> {
        B(T),
        C(Option<U>),
    }
};
let mut s = Structure::new(&di);

// Add an additional where predicate.
s.add_where_predicate(syn::parse_quote!(T: std::fmt::Display));

assert_eq!(
    s.bound_impl(quote!(krate::Trait), quote!{
        fn a() {}
    }).to_string(),
    quote!{
        const _: () = {
            extern crate krate;
            impl<T, U> krate::Trait for A<T, U>
                where T: std::fmt::Display,
                      T: krate::Trait,
                      Option<U>: krate::Trait,
                      U: krate::Trait
            {
                fn a() {}
            }
        };
    }.to_string()
);
```

</div>

</div>

<div id="method.add_bounds" class="section method">

<a href="../src/synstructure/lib.rs.html#1430-1433"
class="src rightside">Source</a>

#### pub fn <a href="#method.add_bounds" class="fn">add_bounds</a>(&mut self, mode: <a href="enum.AddBounds.html" class="enum"
title="enum synstructure::AddBounds">AddBounds</a>) -\> &mut Self

</div>

<div class="docblock">

Specify which bounds should be generated by impl-generating functions
such as `gen_impl`, `bound_impl`, and `unsafe_bound_impl`.

The default behaviour is to generate both field and generic bounds from
type parameters.

##### <a href="#example-6" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A<T, U> {
        B(T),
        C(Option<U>),
    }
};
let mut s = Structure::new(&di);

// Limit bounds to only generics.
s.add_bounds(AddBounds::Generics);

assert_eq!(
    s.bound_impl(quote!(krate::Trait), quote!{
        fn a() {}
    }).to_string(),
    quote!{
        const _: () = {
            extern crate krate;
            impl<T, U> krate::Trait for A<T, U>
                where T: krate::Trait,
                      U: krate::Trait
            {
                fn a() {}
            }
        };
    }.to_string()
);
```

</div>

</div>

<div id="method.filter_variants" class="section method">

<a href="../src/synstructure/lib.rs.html#1469-1479"
class="src rightside">Source</a>

#### pub fn <a href="#method.filter_variants" class="fn">filter_variants</a>\<F\>(&mut self, f: F) -\> &mut Self

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&<a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'\_\>) -\>
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Filter the variants matched by this `Structure` object. This has 2
effects:

- Match arms destructuring these variants will no longer be generated by
  methods on this `Structure`

- Impl blocks created with the `bound_impl` or `unsafe_bound_impl`
  method only consider type parameters referenced in the types of fields
  in non-fitered variants.

##### <a href="#example-7" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A {
        B(i32, i32),
        C(u32),
    }
};

let mut s = Structure::new(&di);

s.filter_variants(|v| v.ast().ident != "B");

assert_eq!(
    s.each(|bi| quote!(println!("{:?}", #bi))).to_string(),

    quote!{
        A::C(ref __binding_0,) => {
            { println!("{:?}", __binding_0) }
        }
        _ => {}
    }.to_string()
);
```

</div>

</div>

<div id="method.drain_filter_variants" class="section method">

<a href="../src/synstructure/lib.rs.html#1523-1541"
class="src rightside">Source</a>

#### pub fn <a href="#method.drain_filter_variants"
class="fn">drain_filter_variants</a>\<F\>(&mut self, f: F) -\> Self

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&<a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'\_\>) -\>
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Iterates all the variants of this `Structure` object and uses a closure
to determine if a variant should be removed. If the closure returns
`true` the variant is removed from the structure. If the closure returns
`false`, the variant remains in the structure.

All the removed variants are moved to a new `Structure` object which is
otherwise identical to the current one. To understand the effects of
removing a variant from a structure check the
[`Structure::filter_variants`](struct.Structure.html#method.filter_variants "method synstructure::Structure::filter_variants")
documentation.

##### <a href="#example-8" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A {
        B(i32, i32),
        C(u32),
    }
};

let mut with_c = Structure::new(&di);

let with_b = with_c.drain_filter_variants(|v| v.ast().ident == "B");

assert_eq!(
    with_c.each(|bi| quote!(println!("{:?}", #bi))).to_string(),

    quote!{
        A::C(ref __binding_0,) => {
            { println!("{:?}", __binding_0) }
        }
    }.to_string()
);

assert_eq!(
    with_b.each(|bi| quote!(println!("{:?}", #bi))).to_string(),

    quote!{
        A::B(ref __binding_0, ref __binding_1,) => {
            { println!("{:?}", __binding_0) }
            { println!("{:?}", __binding_1) }
        }
    }.to_string()
);
```

</div>

</div>

<div id="method.remove_variant" class="section method">

<a href="../src/synstructure/lib.rs.html#1548-1552"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove_variant" class="fn">remove_variant</a>(&mut self, idx: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> &mut Self

</div>

<div class="docblock">

Remove the variant at the given index.

##### <a href="#panics-1" class="doc-anchor">§</a>Panics

Panics if the index is out of range.

</div>

<div id="method.bind_with" class="section method">

<a href="../src/synstructure/lib.rs.html#1584-1592"
class="src rightside">Source</a>

#### pub fn <a href="#method.bind_with" class="fn">bind_with</a>\<F\>(&mut self, f: F) -\> &mut Self

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&<a href="struct.BindingInfo.html" class="struct"
title="struct synstructure::BindingInfo">BindingInfo</a>\<'\_\>) -\>
<a href="enum.BindStyle.html" class="enum"
title="enum synstructure::BindStyle">BindStyle</a>,

</div>

</div>

<div class="docblock">

Updates the `BindStyle` for each of the passed-in fields by calling the
passed-in function for each `BindingInfo`.

##### <a href="#example-9" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A {
        B(i32, i32),
        C(u32),
    }
};
let mut s = Structure::new(&di);

s.bind_with(|bi| BindStyle::RefMut);

assert_eq!(
    s.each(|bi| quote!(println!("{:?}", #bi))).to_string(),

    quote!{
        A::B(ref mut __binding_0, ref mut __binding_1,) => {
            { println!("{:?}", __binding_0) }
            { println!("{:?}", __binding_1) }
        }
        A::C(ref mut __binding_0,) => {
            { println!("{:?}", __binding_0) }
        }
    }.to_string()
);
```

</div>

</div>

<div id="method.binding_name" class="section method">

<a href="../src/synstructure/lib.rs.html#1630-1638"
class="src rightside">Source</a>

#### pub fn <a href="#method.binding_name" class="fn">binding_name</a>\<F\>(&mut self, f: F) -\> &mut Self

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&<a href="../syn/data/struct.Field.html" class="struct"
title="struct syn::data::Field">Field</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\>
<a href="../proc_macro2/struct.Ident.html" class="struct"
title="struct proc_macro2::Ident">Ident</a>,

</div>

</div>

<div class="docblock">

Updates the binding name for each fo the passed-in fields by calling the
passed-in function for each `BindingInfo`.

The function will be called with the `BindingInfo` and its index in the
enclosing variant.

The default name is `__binding_{}` where `{}` is replaced with an
increasing number.

##### <a href="#example-10" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A {
        B{ a: i32, b: i32 },
        C{ a: u32 },
    }
};
let mut s = Structure::new(&di);

s.binding_name(|bi, i| bi.ident.clone().unwrap());

assert_eq!(
    s.each(|bi| quote!(println!("{:?}", #bi))).to_string(),

    quote!{
        A::B{ a: ref a, b: ref b, } => {
            { println!("{:?}", a) }
            { println!("{:?}", b) }
        }
        A::C{ a: ref a, } => {
            { println!("{:?}", a) }
        }
    }.to_string()
);
```

</div>

</div>

<div id="method.referenced_ty_params" class="section method">

<a href="../src/synstructure/lib.rs.html#1667-1675"
class="src rightside">Source</a>

#### pub fn <a href="#method.referenced_ty_params"
class="fn">referenced_ty_params</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html"
class="struct" title="struct alloc::vec::Vec">Vec</a>\<&'a <a href="../proc_macro2/struct.Ident.html" class="struct"
title="struct proc_macro2::Ident">Ident</a>\>

</div>

<div class="docblock">

Returns a list of the type parameters which are refrenced in the types
of non-filtered fields / variants.

##### <a href="#caveat" class="doc-anchor">§</a>Caveat

If the struct contains any macros in type position, all parameters will
be considered bound. This is because we cannot determine which type
parameters are bound by type macros.

##### <a href="#example-11" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A<T, U> {
        B(T, i32),
        C(Option<U>),
    }
};
let mut s = Structure::new(&di);

s.filter_variants(|v| v.ast().ident != "C");

assert_eq!(
    s.referenced_ty_params(),
    &[&quote::format_ident!("T")]
);
```

</div>

</div>

<div id="method.add_impl_generic" class="section method">

<a href="../src/synstructure/lib.rs.html#1713-1716"
class="src rightside">Source</a>

#### pub fn <a href="#method.add_impl_generic" class="fn">add_impl_generic</a>(&mut self, param: <a href="../syn/generics/enum.GenericParam.html" class="enum"
title="enum syn::generics::GenericParam">GenericParam</a>) -\> &mut Self

</div>

<div class="docblock">

Adds an `impl<>` generic parameter. This can be used when the trait to
be derived needs some extra generic parameters.

##### <a href="#example-12" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A<T, U> {
        B(T),
        C(Option<U>),
    }
};
let mut s = Structure::new(&di);
let generic: syn::GenericParam = syn::parse_quote!(X: krate::AnotherTrait);

assert_eq!(
    s.add_impl_generic(generic)
        .bound_impl(quote!(krate::Trait<X>),
        quote!{
                fn a() {}
        }
    ).to_string(),
    quote!{
        const _: () = {
            extern crate krate;
            impl<T, U, X: krate::AnotherTrait> krate::Trait<X> for A<T, U>
                where T : krate :: Trait < X >,
                      Option<U>: krate::Trait<X>,
                      U: krate::Trait<X>
            {
                fn a() {}
            }
        };
    }.to_string()
);
```

</div>

</div>

<div id="method.add_trait_bounds" class="section method">

<a href="../src/synstructure/lib.rs.html#1726-1791"
class="src rightside">Source</a>

#### pub fn <a href="#method.add_trait_bounds" class="fn">add_trait_bounds</a>( &self, bound: &<a href="../syn/generics/struct.TraitBound.html" class="struct"
title="struct syn::generics::TraitBound">TraitBound</a>, where_clause: &mut <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../syn/generics/struct.WhereClause.html" class="struct"
title="struct syn::generics::WhereClause">WhereClause</a>\>, mode: <a href="enum.AddBounds.html" class="enum"
title="enum synstructure::AddBounds">AddBounds</a>, )

</div>

<div class="docblock">

Add trait bounds for a trait with the given path for each type parmaeter
referenced in the types of non-filtered fields.

##### <a href="#caveat-1" class="doc-anchor">§</a>Caveat

If the method contains any macros in type position, all parameters will
be considered bound. This is because we cannot determine which type
parameters are bound by type macros.

</div>

<div id="method.underscore_const" class="section method">

<a href="../src/synstructure/lib.rs.html#1794-1796"
class="src rightside">Source</a>

#### pub fn <a href="#method.underscore_const" class="fn">underscore_const</a>(&mut self, \_enabled: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>) -\> &mut Self

</div>

<div class="docblock">

This method is a no-op, underscore consts are used by default now.

</div>

<div id="method.bound_impl" class="section method">

<a href="../src/synstructure/lib.rs.html#1857-1864"
class="src rightside">Source</a>

#### pub fn <a href="#method.bound_impl" class="fn">bound_impl</a>\<P: <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>, B: <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>\>( &self, path: P, body: B, ) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="docblock">

> NOTE: This methods’ features are superceded by `Structure::gen_impl`.

Creates an `impl` block with the required generic type fields filled in
to implement the trait `path`.

This method also adds where clauses to the impl requiring that all
referenced type parmaeters implement the trait `path`.

##### <a href="#hygiene-and-paths" class="doc-anchor">§</a>Hygiene and Paths

This method wraps the impl block inside of a `const` (see the example
below). In this scope, the first segment of the passed-in path is
`extern crate`-ed in. If you don’t want to generate that `extern crate`
item, use a global path.

This means that if you are implementing `my_crate::Trait`, you simply
write `s.bound_impl(quote!(my_crate::Trait), quote!(...))`, and for the
entirety of the definition, you can refer to your crate as `my_crate`.

##### <a href="#caveat-2" class="doc-anchor">§</a>Caveat

If the method contains any macros in type position, all parameters will
be considered bound. This is because we cannot determine which type
parameters are bound by type macros.

##### <a href="#panics-2" class="doc-anchor">§</a>Panics

Panics if the path string parameter is not a valid `TraitBound`.

##### <a href="#example-13" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A<T, U> {
        B(T),
        C(Option<U>),
    }
};
let mut s = Structure::new(&di);

s.filter_variants(|v| v.ast().ident != "B");

assert_eq!(
    s.bound_impl(quote!(krate::Trait), quote!{
        fn a() {}
    }).to_string(),
    quote!{
        const _: () = {
            extern crate krate;
            impl<T, U> krate::Trait for A<T, U>
                where Option<U>: krate::Trait,
                      U: krate::Trait
            {
                fn a() {}
            }
        };
    }.to_string()
);
```

</div>

</div>

<div id="method.unsafe_bound_impl" class="section method">

<a href="../src/synstructure/lib.rs.html#1925-1932"
class="src rightside">Source</a>

#### pub fn <a href="#method.unsafe_bound_impl" class="fn">unsafe_bound_impl</a>\<P: <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>, B: <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>\>( &self, path: P, body: B, ) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="docblock">

> NOTE: This methods’ features are superceded by `Structure::gen_impl`.

Creates an `impl` block with the required generic type fields filled in
to implement the unsafe trait `path`.

This method also adds where clauses to the impl requiring that all
referenced type parmaeters implement the trait `path`.

##### <a href="#hygiene-and-paths-1" class="doc-anchor">§</a>Hygiene and Paths

This method wraps the impl block inside of a `const` (see the example
below). In this scope, the first segment of the passed-in path is
`extern crate`-ed in. If you don’t want to generate that `extern crate`
item, use a global path.

This means that if you are implementing `my_crate::Trait`, you simply
write `s.bound_impl(quote!(my_crate::Trait), quote!(...))`, and for the
entirety of the definition, you can refer to your crate as `my_crate`.

##### <a href="#caveat-3" class="doc-anchor">§</a>Caveat

If the method contains any macros in type position, all parameters will
be considered bound. This is because we cannot determine which type
parameters are bound by type macros.

##### <a href="#panics-3" class="doc-anchor">§</a>Panics

Panics if the path string parameter is not a valid `TraitBound`.

##### <a href="#example-14" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A<T, U> {
        B(T),
        C(Option<U>),
    }
};
let mut s = Structure::new(&di);

s.filter_variants(|v| v.ast().ident != "B");

assert_eq!(
    s.unsafe_bound_impl(quote!(krate::Trait), quote!{
        fn a() {}
    }).to_string(),
    quote!{
        const _: () = {
            extern crate krate;
            unsafe impl<T, U> krate::Trait for A<T, U>
                where Option<U>: krate::Trait,
                      U: krate::Trait
            {
                fn a() {}
            }
        };
    }.to_string()
);
```

</div>

</div>

<div id="method.unbound_impl" class="section method">

<a href="../src/synstructure/lib.rs.html#1983-1990"
class="src rightside">Source</a>

#### pub fn <a href="#method.unbound_impl" class="fn">unbound_impl</a>\<P: <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>, B: <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>\>( &self, path: P, body: B, ) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="docblock">

> NOTE: This methods’ features are superceded by `Structure::gen_impl`.

Creates an `impl` block with the required generic type fields filled in
to implement the trait `path`.

This method will not add any where clauses to the impl.

##### <a href="#hygiene-and-paths-2" class="doc-anchor">§</a>Hygiene and Paths

This method wraps the impl block inside of a `const` (see the example
below). In this scope, the first segment of the passed-in path is
`extern crate`-ed in. If you don’t want to generate that `extern crate`
item, use a global path.

This means that if you are implementing `my_crate::Trait`, you simply
write `s.bound_impl(quote!(my_crate::Trait), quote!(...))`, and for the
entirety of the definition, you can refer to your crate as `my_crate`.

##### <a href="#panics-4" class="doc-anchor">§</a>Panics

Panics if the path string parameter is not a valid `TraitBound`.

##### <a href="#example-15" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A<T, U> {
        B(T),
        C(Option<U>),
    }
};
let mut s = Structure::new(&di);

s.filter_variants(|v| v.ast().ident != "B");

assert_eq!(
    s.unbound_impl(quote!(krate::Trait), quote!{
        fn a() {}
    }).to_string(),
    quote!{
        const _: () = {
            extern crate krate;
            impl<T, U> krate::Trait for A<T, U> {
                fn a() {}
            }
        };
    }.to_string()
);
```

</div>

</div>

<div id="method.unsafe_unbound_impl" class="section method">

<a href="../src/synstructure/lib.rs.html#2042-2049"
class="src rightside">Source</a>

#### pub fn <a href="#method.unsafe_unbound_impl" class="fn">unsafe_unbound_impl</a>\<P: <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>, B: <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>\>( &self, path: P, body: B, ) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<span class="item-info"></span>

<div class="stab deprecated">

👎Deprecated

</div>

<div class="docblock">

> NOTE: This methods’ features are superceded by `Structure::gen_impl`.

Creates an `impl` block with the required generic type fields filled in
to implement the unsafe trait `path`.

This method will not add any where clauses to the impl.

##### <a href="#hygiene-and-paths-3" class="doc-anchor">§</a>Hygiene and Paths

This method wraps the impl block inside of a `const` (see the example
below). In this scope, the first segment of the passed-in path is
`extern crate`-ed in. If you don’t want to generate that `extern crate`
item, use a global path.

This means that if you are implementing `my_crate::Trait`, you simply
write `s.bound_impl(quote!(my_crate::Trait), quote!(...))`, and for the
entirety of the definition, you can refer to your crate as `my_crate`.

##### <a href="#panics-5" class="doc-anchor">§</a>Panics

Panics if the path string parameter is not a valid `TraitBound`.

##### <a href="#example-16" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A<T, U> {
        B(T),
        C(Option<U>),
    }
};
let mut s = Structure::new(&di);

s.filter_variants(|v| v.ast().ident != "B");

assert_eq!(
    s.unsafe_unbound_impl(quote!(krate::Trait), quote!{
        fn a() {}
    }).to_string(),
    quote!{
        const _: () = {
            extern crate krate;
            unsafe impl<T, U> krate::Trait for A<T, U> {
                fn a() {}
            }
        };
    }.to_string()
);
```

</div>

</div>

<div id="method.gen_impl" class="section method">

<a href="../src/synstructure/lib.rs.html#2295-2301"
class="src rightside">Source</a>

#### pub fn <a href="#method.gen_impl" class="fn">gen_impl</a>(&self, cfg: <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="docblock">

Generate an impl block for the given struct. This impl block will
automatically use hygiene tricks to avoid polluting the caller’s
namespace, and will automatically add trait bounds for generic type
parameters.

##### <a href="#syntax" class="doc-anchor">§</a>Syntax

This function accepts its arguments as a `TokenStream`. The recommended
way to call this function is passing the result of invoking the `quote!`
macro to it.

<div class="example-wrap ignore">

<a href="#" class="tooltip" title="This example is not tested">ⓘ</a>

``` rust
s.gen_impl(quote! {
    // You can write any items which you want to import into scope here.
    // For example, you may want to include an `extern crate` for the
    // crate which implements your trait. These items will only be
    // visible to the code you generate, and won't be exposed to the
    // consuming crate
    extern crate krate;

    // You can also add `use` statements here to bring types or traits
    // into scope.
    //
    // WARNING: Try not to use common names here, because the stable
    // version of syn does not support hygiene and you could accidentally
    // shadow types from the caller crate.
    use krate::Trait as MyTrait;

    // The actual impl block is a `gen impl` or `gen unsafe impl` block.
    // You can use `@Self` to refer to the structure's type.
    gen impl MyTrait for @Self {
        fn f(&self) { ... }
    }
})
```

</div>

The most common usage of this trait involves loading the crate the
target trait comes from with `extern crate`, and then invoking a
`gen impl` block.

##### <a href="#hygiene" class="doc-anchor">§</a>Hygiene

This method tries to handle hygiene intelligently for both stable and
unstable proc-macro implementations, however there are visible
differences.

The output of every `gen_impl` function is wrapped in a dummy `const`
value, to ensure that it is given its own scope, and any values brought
into scope are not leaked to the calling crate.

By default, the above invocation may generate an output like the
following:

<div class="example-wrap ignore">

<a href="#" class="tooltip" title="This example is not tested">ⓘ</a>

``` rust
const _: () = {
    extern crate krate;
    use krate::Trait as MyTrait;
    impl<T> MyTrait for Struct<T> where T: MyTrait {
        fn f(&self) { ... }
    }
};
```

</div>

###### <a href="#using-the-std-crate" class="doc-anchor">§</a>Using the `std` crate

If you are using `quote!()` to implement your trait, with the
`proc-macro2/nightly` feature, `std` isn’t considered to be in scope for
your macro. This means that if you use types from `std` in your
procedural macro, you’ll want to explicitly load it with an
`extern crate std;`.

###### <a href="#absolute-paths" class="doc-anchor">§</a>Absolute paths

You should generally avoid using absolute paths in your generated code,
as they will resolve very differently when using the stable and nightly
versions of `proc-macro2`. Instead, load the crates you need to use
explictly with `extern crate` and

##### <a href="#trait-bounds" class="doc-anchor">§</a>Trait Bounds

This method will automatically add trait bounds for any type parameters
which are referenced within the types of non-ignored fields.

Additional type parameters may be added with the generics syntax after
the `impl` keyword.

###### <a href="#type-macro-caveat" class="doc-anchor">§</a>Type Macro Caveat

If the method contains any macros in type position, all parameters will
be considered bound. This is because we cannot determine which type
parameters are bound by type macros.

##### <a href="#errors" class="doc-anchor">§</a>Errors

This function will generate a `compile_error!` if additional type
parameters added by `impl<..>` conflict with generic type parameters on
the original struct.

##### <a href="#panics-6" class="doc-anchor">§</a>Panics

This function will panic if the input `TokenStream` is not well-formed.

##### <a href="#example-usage" class="doc-anchor">§</a>Example Usage

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A<T, U> {
        B(T),
        C(Option<U>),
    }
};
let mut s = Structure::new(&di);

s.filter_variants(|v| v.ast().ident != "B");

assert_eq!(
    s.gen_impl(quote! {
        extern crate krate;
        gen impl krate::Trait for @Self {
            fn a() {}
        }
    }).to_string(),
    quote!{
        const _: () = {
            extern crate krate;
            impl<T, U> krate::Trait for A<T, U>
            where
                Option<U>: krate::Trait,
                U: krate::Trait
            {
                fn a() {}
            }
        };
    }.to_string()
);

// NOTE: You can also add extra generics after the impl
assert_eq!(
    s.gen_impl(quote! {
        extern crate krate;
        gen impl<X: krate::OtherTrait> krate::Trait<X> for @Self
        where
            X: Send + Sync,
        {
            fn a() {}
        }
    }).to_string(),
    quote!{
        const _: () = {
            extern crate krate;
            impl<X: krate::OtherTrait, T, U> krate::Trait<X> for A<T, U>
            where
                X: Send + Sync,
                Option<U>: krate::Trait<X>,
                U: krate::Trait<X>
            {
                fn a() {}
            }
        };
    }.to_string()
);

// NOTE: you can generate multiple traits with a single call
assert_eq!(
    s.gen_impl(quote! {
        extern crate krate;

        gen impl krate::Trait for @Self {
            fn a() {}
        }

        gen impl krate::OtherTrait for @Self {
            fn b() {}
        }
    }).to_string(),
    quote!{
        const _: () = {
            extern crate krate;
            impl<T, U> krate::Trait for A<T, U>
            where
                Option<U>: krate::Trait,
                U: krate::Trait
            {
                fn a() {}
            }

            impl<T, U> krate::OtherTrait for A<T, U>
            where
                Option<U>: krate::OtherTrait,
                U: krate::OtherTrait
            {
                fn b() {}
            }
        };
    }.to_string()
);
```

</div>

Use `add_bounds` to change which bounds are generated.

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-Structure%3C'a%3E" class="section impl">

<a href="../src/synstructure/lib.rs.html#995"
class="src rightside">Source</a><a href="#impl-Clone-for-Structure%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="struct.Structure.html" class="struct"
title="struct synstructure::Structure">Structure</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../src/synstructure/lib.rs.html#995"
class="src rightside">Source</a><a href="#method.clone" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone"
class="fn">clone</a>(&self) -\> <a href="struct.Structure.html" class="struct"
title="struct synstructure::Structure">Structure</a>\<'a\>

</div>

<div class="docblock">

Returns a duplicate of the value. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone)

</div>

<div id="method.clone_from" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#245-247"
class="src">Source</a></span><a href="#method.clone_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from"
class="fn">clone_from</a>(&mut self, source: &Self)

</div>

<div class="docblock">

Performs copy-assignment from `source`. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from)

</div>

</div>

<div id="impl-Debug-for-Structure%3C'a%3E" class="section impl">

<a href="../src/synstructure/lib.rs.html#995"
class="src rightside">Source</a><a href="#impl-Debug-for-Structure%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.Structure.html" class="struct"
title="struct synstructure::Structure">Structure</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../src/synstructure/lib.rs.html#995"
class="src rightside">Source</a><a href="#method.fmt" class="anchor">§</a>

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

<div id="impl-Hash-for-Structure%3C'a%3E" class="section impl">

<a href="../src/synstructure/lib.rs.html#995"
class="src rightside">Source</a><a href="#impl-Hash-for-Structure%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> for <a href="struct.Structure.html" class="struct"
title="struct synstructure::Structure">Structure</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.hash" class="section method trait-impl">

<a href="../src/synstructure/lib.rs.html#995"
class="src rightside">Source</a><a href="#method.hash" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#tymethod.hash"
class="fn">hash</a>\<\_\_H: <a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html"
class="trait" title="trait core::hash::Hasher">Hasher</a>\>(&self, state: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut __H</a>)

</div>

<div class="docblock">

Feeds this value into the given
[`Hasher`](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html "trait core::hash::Hasher").
[Read
more](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#tymethod.hash)

</div>

<div id="method.hash_slice" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.3.0">1.3.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/hash/mod.rs.html#235-237"
class="src">Source</a></span><a href="#method.hash_slice" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#method.hash_slice"
class="fn">hash_slice</a>\<H\>(data: &\[Self\], state: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut H</a>)

<div class="where">

where H:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html"
class="trait" title="trait core::hash::Hasher">Hasher</a>, Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Feeds a slice of this type into the given
[`Hasher`](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html "trait core::hash::Hasher").
[Read
more](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#method.hash_slice)

</div>

</div>

<div id="impl-PartialEq-for-Structure%3C'a%3E" class="section impl">

<a href="../src/synstructure/lib.rs.html#995"
class="src rightside">Source</a><a href="#impl-PartialEq-for-Structure%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a> for <a href="struct.Structure.html" class="struct"
title="struct synstructure::Structure">Structure</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.eq" class="section method trait-impl">

<a href="../src/synstructure/lib.rs.html#995"
class="src rightside">Source</a><a href="#method.eq" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#tymethod.eq"
class="fn">eq</a>(&self, other: &<a href="struct.Structure.html" class="struct"
title="struct synstructure::Structure">Structure</a>\<'a\>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `self` and `other` values to be equal, and is used by `==`.

</div>

<div id="method.ne" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#264"
class="src">Source</a></span><a href="#method.ne" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#method.ne"
class="fn">ne</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `!=`. The default implementation is almost always sufficient,
and should not be overridden without very good reason.

</div>

</div>

<div id="impl-Eq-for-Structure%3C'a%3E" class="section impl">

<a href="../src/synstructure/lib.rs.html#995"
class="src rightside">Source</a><a href="#impl-Eq-for-Structure%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> for <a href="struct.Structure.html" class="struct"
title="struct synstructure::Structure">Structure</a>\<'a\>

</div>

<div id="impl-StructuralPartialEq-for-Structure%3C'a%3E"
class="section impl">

<a href="../src/synstructure/lib.rs.html#995"
class="src rightside">Source</a><a href="#impl-StructuralPartialEq-for-Structure%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a
href="https://doc.rust-lang.org/1.92.0/core/marker/trait.StructuralPartialEq.html"
class="trait"
title="trait core::marker::StructuralPartialEq">StructuralPartialEq</a> for <a href="struct.Structure.html" class="struct"
title="struct synstructure::Structure">Structure</a>\<'a\>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-Structure%3C'a%3E" class="section impl">

<a href="#impl-Freeze-for-Structure%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.Structure.html" class="struct"
title="struct synstructure::Structure">Structure</a>\<'a\>

</div>

<div id="impl-RefUnwindSafe-for-Structure%3C'a%3E" class="section impl">

<a href="#impl-RefUnwindSafe-for-Structure%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.Structure.html" class="struct"
title="struct synstructure::Structure">Structure</a>\<'a\>

</div>

<div id="impl-Send-for-Structure%3C'a%3E" class="section impl">

<a href="#impl-Send-for-Structure%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.Structure.html" class="struct"
title="struct synstructure::Structure">Structure</a>\<'a\>

</div>

<div id="impl-Sync-for-Structure%3C'a%3E" class="section impl">

<a href="#impl-Sync-for-Structure%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.Structure.html" class="struct"
title="struct synstructure::Structure">Structure</a>\<'a\>

</div>

<div id="impl-Unpin-for-Structure%3C'a%3E" class="section impl">

<a href="#impl-Unpin-for-Structure%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.Structure.html" class="struct"
title="struct synstructure::Structure">Structure</a>\<'a\>

</div>

<div id="impl-UnwindSafe-for-Structure%3C'a%3E" class="section impl">

<a href="#impl-UnwindSafe-for-Structure%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.Structure.html" class="struct"
title="struct synstructure::Structure">Structure</a>\<'a\>

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

<div id="impl-CloneToUninit-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#515"
class="src rightside">Source</a><a href="#impl-CloneToUninit-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html"
class="trait" title="trait core::clone::CloneToUninit">CloneToUninit</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.clone_to_uninit" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#517"
class="src rightside">Source</a><a href="#method.clone_to_uninit" class="anchor">§</a>

#### unsafe fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit"
class="fn">clone_to_uninit</a>(&self, dest: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.pointer.html"
class="primitive">*mut</a> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`clone_to_uninit`)

</div>

<div class="docblock">

Performs copy-assignment from `self` to `dest`. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit)

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

<div id="impl-ToOwned-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#85-87"
class="src rightside">Source</a><a href="#impl-ToOwned-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html"
class="trait" title="trait alloc::borrow::ToOwned">ToOwned</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Owned"
class="section associatedtype trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#89"
class="src rightside">Source</a><a href="#associatedtype.Owned" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#associatedtype.Owned"
class="associatedtype">Owned</a> = T

</div>

<div class="docblock">

The resulting type after obtaining ownership.

</div>

<div id="method.to_owned" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#90"
class="src rightside">Source</a><a href="#method.to_owned" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#tymethod.to_owned"
class="fn">to_owned</a>(&self) -\> T

</div>

<div class="docblock">

Creates owned data from borrowed data, usually by cloning. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#tymethod.to_owned)

</div>

<div id="method.clone_into" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#94"
class="src rightside">Source</a><a href="#method.clone_into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#method.clone_into"
class="fn">clone_into</a>(&self, target: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>)

</div>

<div class="docblock">

Uses borrowed data to replace owned data, usually by cloning. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#method.clone_into)

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
