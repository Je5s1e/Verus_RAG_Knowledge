<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[synstructure](index.html)

</div>

# Struct <span class="struct">VariantInfo</span> Copy item path

<span class="sub-heading"><a href="../src/synstructure/lib.rs.html#427-434" class="src">Source</a>
</span>

</div>

``` rust
pub struct VariantInfo<'a> {
    pub prefix: Option<&'a Ident>,
    /* private fields */
}
```

Expand description

<div class="docblock">

A wrapper around a `syn::DeriveInput`’s variant which provides utilities
for destructuring `Variant`s with `match` expressions.

</div>

## Fields<a href="#fields" class="anchor">§</a>

<span id="structfield.prefix"
class="structfield section-header"><a href="#structfield.prefix" class="anchor field">§</a>`prefix: `<a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option"><code>Option</code></a>`<&'a `<a href="../proc_macro2/struct.Ident.html" class="struct"
title="struct proc_macro2::Ident"><code>Ident</code></a>`>`</span>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-VariantInfo%3C'a%3E" class="section impl">

<a href="../src/synstructure/lib.rs.html#480-991"
class="src rightside">Source</a><a href="#impl-VariantInfo%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.bindings" class="section method">

<a href="../src/synstructure/lib.rs.html#520-522"
class="src rightside">Source</a>

#### pub fn <a href="#method.bindings" class="fn">bindings</a>(&self) -\> &\[<a href="struct.BindingInfo.html" class="struct"
title="struct synstructure::BindingInfo">BindingInfo</a>\<'a\>\]

</div>

<div class="docblock">

Returns a slice of the bindings in this Variant.

</div>

<div id="method.bindings_mut" class="section method">

<a href="../src/synstructure/lib.rs.html#525-527"
class="src rightside">Source</a>

#### pub fn <a href="#method.bindings_mut" class="fn">bindings_mut</a>(&mut self) -\> &mut \[<a href="struct.BindingInfo.html" class="struct"
title="struct synstructure::BindingInfo">BindingInfo</a>\<'a\>\]

</div>

<div class="docblock">

Returns a mut slice of the bindings in this Variant.

</div>

<div id="method.ast" class="section method">

<a href="../src/synstructure/lib.rs.html#531-533"
class="src rightside">Source</a>

#### pub fn <a href="#method.ast" class="fn">ast</a>(&self) -\> <a href="struct.VariantAst.html" class="struct"
title="struct synstructure::VariantAst">VariantAst</a>\<'a\>

</div>

<div class="docblock">

Returns a `VariantAst` object which contains references to the
underlying `syn` AST node which this `Variant` was created from.

</div>

<div id="method.omitted_bindings" class="section method">

<a href="../src/synstructure/lib.rs.html#536-538"
class="src rightside">Source</a>

#### pub fn <a href="#method.omitted_bindings" class="fn">omitted_bindings</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

True if any bindings were omitted due to a `filter` call.

</div>

<div id="method.pat" class="section method">

<a href="../src/synstructure/lib.rs.html#560-599"
class="src rightside">Source</a>

#### pub fn <a href="#method.pat" class="fn">pat</a>(&self) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="docblock">

Generates the match-arm pattern which could be used to match against
this Variant.

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
    s.variants()[0].pat().to_string(),
    quote!{
        A::B(ref __binding_0, ref __binding_1,)
    }.to_string()
);
```

</div>

</div>

<div id="method.construct" class="section method">

<a href="../src/synstructure/lib.rs.html#633-666"
class="src rightside">Source</a>

#### pub fn <a href="#method.construct" class="fn">construct</a>\<F, T\>(&self, func: F) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&<a href="../syn/data/struct.Field.html" class="struct"
title="struct syn::data::Field">Field</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> T, T:
<a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>,

</div>

</div>

<div class="docblock">

Generates the token stream required to construct the current variant.

The init array initializes each of the fields in the order they are
written in `variant.ast().fields`.

##### <a href="#example-1" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A {
        B(usize, usize),
        C{ v: usize },
    }
};
let s = Structure::new(&di);

assert_eq!(
    s.variants()[0].construct(|_, i| quote!(#i)).to_string(),

    quote!{
        A::B(0usize, 1usize,)
    }.to_string()
);

assert_eq!(
    s.variants()[1].construct(|_, i| quote!(#i)).to_string(),

    quote!{
        A::C{ v: 0usize, }
    }.to_string()
);
```

</div>

</div>

<div id="method.each" class="section method">

<a href="../src/synstructure/lib.rs.html#696-709"
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
`BindingInfo`. and generating a `match` arm which evaluates the returned
tokens.

This method will ignore fields which are ignored through the `filter`
method.

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
    s.variants()[0].each(|bi| quote!(println!("{:?}", #bi))).to_string(),

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

<div id="method.fold" class="section method">

<a href="../src/synstructure/lib.rs.html#739-751"
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
result of the previous call, and a `BindingInfo`. generating a `match`
arm which evaluates to the resulting tokens.

This method will ignore fields which are ignored through the `filter`
method.

##### <a href="#example-3" class="doc-anchor">§</a>Example

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
    s.variants()[0].fold(quote!(0), |acc, bi| quote!(#acc + #bi)).to_string(),

    quote!{
        A::B(ref __binding_0, ref __binding_1,) => {
            0 + __binding_0 + __binding_1
        }
    }.to_string()
);
```

</div>

</div>

<div id="method.filter" class="section method">

<a href="../src/synstructure/lib.rs.html#790-796"
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

Filter the bindings created by this `Variant` object. This has 2
effects:

- The bindings will no longer appear in match arms generated by methods
  on this `Variant` or its subobjects.

- Impl blocks created with the `bound_impl` or `unsafe_bound_impl`
  method only consider type parameters referenced in the types of
  non-filtered fields.

##### <a href="#example-4" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A {
        B{ a: i32, b: i32 },
        C{ a: u32 },
    }
};
let mut s = Structure::new(&di);

s.variants_mut()[0].filter(|bi| {
    bi.ast().ident == Some(quote::format_ident!("b"))
});

assert_eq!(
    s.each(|bi| quote!(println!("{:?}", #bi))).to_string(),

    quote!{
        A::B{ b: ref __binding_1, .. } => {
            { println!("{:?}", __binding_1) }
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

<a href="../src/synstructure/lib.rs.html#844-861"
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

Iterates all the bindings of this `Variant` object and uses a closure to
determine if a binding should be removed. If the closure returns `true`
the binding is removed from the variant. If the closure returns `false`,
the binding remains in the variant.

All the removed bindings are moved to a new `Variant` object which is
otherwise identical to the current one. To understand the effects of
removing a binding from a variant check the
[`VariantInfo::filter`](struct.VariantInfo.html#method.filter "method synstructure::VariantInfo::filter")
documentation.

##### <a href="#example-5" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A {
        B{ a: i32, b: i32 },
        C{ a: u32 },
    }
};
let mut s = Structure::new(&di);

let mut with_b = &mut s.variants_mut()[0];

let with_a = with_b.drain_filter(|bi| {
    bi.ast().ident == Some(quote::format_ident!("a"))
});

assert_eq!(
    with_a.each(|bi| quote!(println!("{:?}", #bi))).to_string(),

    quote!{
        A::B{ a: ref __binding_0, .. } => {
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
    }.to_string()
);
```

</div>

</div>

<div id="method.remove_binding" class="section method">

<a href="../src/synstructure/lib.rs.html#868-871"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove_binding" class="fn">remove_binding</a>(&mut self, idx: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> &mut Self

</div>

<div class="docblock">

Remove the binding at the given index.

##### <a href="#panics" class="doc-anchor">§</a>Panics

Panics if the index is out of range.

</div>

<div id="method.bind_with" class="section method">

<a href="../src/synstructure/lib.rs.html#903-911"
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

##### <a href="#example-6" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A {
        B(i32, i32),
        C(u32),
    }
};
let mut s = Structure::new(&di);

s.variants_mut()[0].bind_with(|bi| BindStyle::RefMut);

assert_eq!(
    s.each(|bi| quote!(println!("{:?}", #bi))).to_string(),

    quote!{
        A::B(ref mut __binding_0, ref mut __binding_1,) => {
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

<div id="method.binding_name" class="section method">

<a href="../src/synstructure/lib.rs.html#949-957"
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

##### <a href="#example-7" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    enum A {
        B{ a: i32, b: i32 },
        C{ a: u32 },
    }
};
let mut s = Structure::new(&di);

s.variants_mut()[0].binding_name(|bi, i| bi.ident.clone().unwrap());

assert_eq!(
    s.each(|bi| quote!(println!("{:?}", #bi))).to_string(),

    quote!{
        A::B{ a: ref a, b: ref b, } => {
            { println!("{:?}", a) }
            { println!("{:?}", b) }
        }
        A::C{ a: ref __binding_0, } => {
            { println!("{:?}", __binding_0) }
        }
    }.to_string()
);
```

</div>

</div>

<div id="method.referenced_ty_params" class="section method">

<a href="../src/synstructure/lib.rs.html#984-990"
class="src rightside">Source</a>

#### pub fn <a href="#method.referenced_ty_params"
class="fn">referenced_ty_params</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html"
class="struct" title="struct alloc::vec::Vec">Vec</a>\<&'a <a href="../proc_macro2/struct.Ident.html" class="struct"
title="struct proc_macro2::Ident">Ident</a>\>

</div>

<div class="docblock">

Returns a list of the type parameters which are referenced in this
field’s type.

##### <a href="#caveat" class="doc-anchor">§</a>Caveat

If the field contains any macros in type position, all parameters will
be considered bound. This is because we cannot determine which type
parameters are bound by type macros.

##### <a href="#example-8" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let di: syn::DeriveInput = syn::parse_quote! {
    struct A<T, U> {
        a: Option<T>,
        b: U,
    }
};
let mut s = Structure::new(&di);

assert_eq!(
    s.variants()[0].bindings()[0].referenced_ty_params(),
    &[&quote::format_ident!("T")]
);
```

</div>

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-VariantInfo%3C'a%3E" class="section impl">

<a href="../src/synstructure/lib.rs.html#426"
class="src rightside">Source</a><a href="#impl-Clone-for-VariantInfo%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../src/synstructure/lib.rs.html#426"
class="src rightside">Source</a><a href="#method.clone" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone"
class="fn">clone</a>(&self) -\> <a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>

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

<div id="impl-Debug-for-VariantInfo%3C'a%3E" class="section impl">

<a href="../src/synstructure/lib.rs.html#426"
class="src rightside">Source</a><a href="#impl-Debug-for-VariantInfo%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../src/synstructure/lib.rs.html#426"
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

<div id="impl-Hash-for-VariantInfo%3C'a%3E" class="section impl">

<a href="../src/synstructure/lib.rs.html#426"
class="src rightside">Source</a><a href="#impl-Hash-for-VariantInfo%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> for <a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.hash" class="section method trait-impl">

<a href="../src/synstructure/lib.rs.html#426"
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

<div id="impl-PartialEq-for-VariantInfo%3C'a%3E" class="section impl">

<a href="../src/synstructure/lib.rs.html#426"
class="src rightside">Source</a><a href="#impl-PartialEq-for-VariantInfo%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a> for <a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.eq" class="section method trait-impl">

<a href="../src/synstructure/lib.rs.html#426"
class="src rightside">Source</a><a href="#method.eq" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#tymethod.eq"
class="fn">eq</a>(&self, other: &<a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
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

<div id="impl-Eq-for-VariantInfo%3C'a%3E" class="section impl">

<a href="../src/synstructure/lib.rs.html#426"
class="src rightside">Source</a><a href="#impl-Eq-for-VariantInfo%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> for <a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>

</div>

<div id="impl-StructuralPartialEq-for-VariantInfo%3C'a%3E"
class="section impl">

<a href="../src/synstructure/lib.rs.html#426"
class="src rightside">Source</a><a href="#impl-StructuralPartialEq-for-VariantInfo%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a
href="https://doc.rust-lang.org/1.92.0/core/marker/trait.StructuralPartialEq.html"
class="trait"
title="trait core::marker::StructuralPartialEq">StructuralPartialEq</a> for <a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-VariantInfo%3C'a%3E" class="section impl">

<a href="#impl-Freeze-for-VariantInfo%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>

</div>

<div id="impl-RefUnwindSafe-for-VariantInfo%3C'a%3E"
class="section impl">

<a href="#impl-RefUnwindSafe-for-VariantInfo%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>

</div>

<div id="impl-Send-for-VariantInfo%3C'a%3E" class="section impl">

<a href="#impl-Send-for-VariantInfo%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>

</div>

<div id="impl-Sync-for-VariantInfo%3C'a%3E" class="section impl">

<a href="#impl-Sync-for-VariantInfo%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>

</div>

<div id="impl-Unpin-for-VariantInfo%3C'a%3E" class="section impl">

<a href="#impl-Unpin-for-VariantInfo%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>

</div>

<div id="impl-UnwindSafe-for-VariantInfo%3C'a%3E" class="section impl">

<a href="#impl-UnwindSafe-for-VariantInfo%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.VariantInfo.html" class="struct"
title="struct synstructure::VariantInfo">VariantInfo</a>\<'a\>

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
