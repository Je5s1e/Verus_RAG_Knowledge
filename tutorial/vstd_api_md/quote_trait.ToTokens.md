<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[quote](index.html)

</div>

# Trait <span class="trait">ToTokens</span> Copy item path

<span class="sub-heading"><a href="../src/quote/to_tokens.rs.html#12-75" class="src">Source</a>
</span>

</div>

``` rust
pub trait ToTokens {
    // Required method
    fn to_tokens(&self, tokens: &mut TokenStream);

    // Provided methods
    fn to_token_stream(&self) -> TokenStream { ... }
    fn into_token_stream(self) -> TokenStream
       where Self: Sized { ... }
}
```

Expand description

<div class="docblock">

Types that can be interpolated inside a `quote!` invocation.

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.to_tokens" class="section method">

<a href="../src/quote/to_tokens.rs.html#53"
class="src rightside">Source</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

<div class="docblock">

Write `self` to the given `TokenStream`.

The token append methods provided by the
[`TokenStreamExt`](trait.TokenStreamExt.html "trait quote::TokenStreamExt")
extension trait may be useful for implementing `ToTokens`.

##### <a href="#example" class="doc-anchor">§</a>Example

Example implementation for a struct representing Rust paths like
`std::cmp::PartialEq`:

<div class="example-wrap">

``` rust
use proc_macro2::{TokenTree, Spacing, Span, Punct, TokenStream};
use quote::{TokenStreamExt, ToTokens};

pub struct Path {
    pub global: bool,
    pub segments: Vec<PathSegment>,
}

impl ToTokens for Path {
    fn to_tokens(&self, tokens: &mut TokenStream) {
        for (i, segment) in self.segments.iter().enumerate() {
            if i > 0 || self.global {
                // Double colon `::`
                tokens.append(Punct::new(':', Spacing::Joint));
                tokens.append(Punct::new(':', Spacing::Alone));
            }
            segment.to_tokens(tokens);
        }
    }
}
```

</div>

</div>

</div>

## Provided Methods<a href="#provided-methods" class="anchor">§</a>

<div class="methods">

<div id="method.to_token_stream" class="section method">

<a href="../src/quote/to_tokens.rs.html#59-63"
class="src rightside">Source</a>

#### fn <a href="#method.to_token_stream" class="fn">to_token_stream</a>(&self) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="docblock">

Convert `self` directly into a `TokenStream` object.

This method is implicitly implemented using `to_tokens`, and acts as a
convenience method for consumers of the `ToTokens` trait.

</div>

<div id="method.into_token_stream" class="section method">

<a href="../src/quote/to_tokens.rs.html#69-74"
class="src rightside">Source</a>

#### fn <a href="#method.into_token_stream" class="fn">into_token_stream</a>(self) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Convert `self` directly into a `TokenStream` object.

This method is implicitly implemented using `to_tokens`, and acts as a
convenience method for consumers of the `ToTokens` trait.

</div>

</div>

## Implementations on Foreign Types<a href="#foreign-impls" class="anchor">§</a>

<div id="impl-ToTokens-for-TokenTree" class="section impl">

<a href="../src/quote/to_tokens.rs.html#260-264"
class="src rightside">Source</a><a href="#impl-ToTokens-for-TokenTree" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="../proc_macro2/enum.TokenTree.html" class="enum"
title="enum proc_macro2::TokenTree">TokenTree</a>

</div>

<div class="impl-items">

<div id="method.to_tokens" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#261-263"
class="src rightside">Source</a><a href="#method.to_tokens" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-bool" class="section impl">

<a href="../src/quote/to_tokens.rs.html#217-222"
class="src rightside">Source</a><a href="#impl-ToTokens-for-bool" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-1" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#218-221"
class="src rightside">Source</a><a href="#method.to_tokens-1" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-char" class="section impl">

<a href="../src/quote/to_tokens.rs.html#211-215"
class="src rightside">Source</a><a href="#impl-ToTokens-for-char" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-2" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#212-214"
class="src rightside">Source</a><a href="#method.to_tokens-2" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-f32" class="section impl">

<a href="../src/quote/to_tokens.rs.html#199-203"
class="src rightside">Source</a><a href="#impl-ToTokens-for-f32" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.f32.html"
class="primitive">f32</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-3" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#200-202"
class="src rightside">Source</a><a href="#method.to_tokens-3" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-f64" class="section impl">

<a href="../src/quote/to_tokens.rs.html#205-209"
class="src rightside">Source</a><a href="#impl-ToTokens-for-f64" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.f64.html"
class="primitive">f64</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-4" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#206-208"
class="src rightside">Source</a><a href="#method.to_tokens-4" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-i8" class="section impl">

<a href="../src/quote/to_tokens.rs.html#127-131"
class="src rightside">Source</a><a href="#impl-ToTokens-for-i8" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-5" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#128-130"
class="src rightside">Source</a><a href="#method.to_tokens-5" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-i16" class="section impl">

<a href="../src/quote/to_tokens.rs.html#133-137"
class="src rightside">Source</a><a href="#impl-ToTokens-for-i16" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-6" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#134-136"
class="src rightside">Source</a><a href="#method.to_tokens-6" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-i32" class="section impl">

<a href="../src/quote/to_tokens.rs.html#139-143"
class="src rightside">Source</a><a href="#impl-ToTokens-for-i32" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-7" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#140-142"
class="src rightside">Source</a><a href="#method.to_tokens-7" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-i64" class="section impl">

<a href="../src/quote/to_tokens.rs.html#145-149"
class="src rightside">Source</a><a href="#impl-ToTokens-for-i64" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-8" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#146-148"
class="src rightside">Source</a><a href="#method.to_tokens-8" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-i128" class="section impl">

<a href="../src/quote/to_tokens.rs.html#151-155"
class="src rightside">Source</a><a href="#impl-ToTokens-for-i128" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-9" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#152-154"
class="src rightside">Source</a><a href="#method.to_tokens-9" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-isize" class="section impl">

<a href="../src/quote/to_tokens.rs.html#157-161"
class="src rightside">Source</a><a href="#impl-ToTokens-for-isize" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-10" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#158-160"
class="src rightside">Source</a><a href="#method.to_tokens-10" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-str" class="section impl">

<a href="../src/quote/to_tokens.rs.html#115-119"
class="src rightside">Source</a><a href="#impl-ToTokens-for-str" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-11" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#116-118"
class="src rightside">Source</a><a href="#method.to_tokens-11" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-u8" class="section impl">

<a href="../src/quote/to_tokens.rs.html#163-167"
class="src rightside">Source</a><a href="#impl-ToTokens-for-u8" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-12" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#164-166"
class="src rightside">Source</a><a href="#method.to_tokens-12" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-u16" class="section impl">

<a href="../src/quote/to_tokens.rs.html#169-173"
class="src rightside">Source</a><a href="#impl-ToTokens-for-u16" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-13" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#170-172"
class="src rightside">Source</a><a href="#method.to_tokens-13" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-u32" class="section impl">

<a href="../src/quote/to_tokens.rs.html#175-179"
class="src rightside">Source</a><a href="#impl-ToTokens-for-u32" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-14" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#176-178"
class="src rightside">Source</a><a href="#method.to_tokens-14" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-u64" class="section impl">

<a href="../src/quote/to_tokens.rs.html#181-185"
class="src rightside">Source</a><a href="#impl-ToTokens-for-u64" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-15" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#182-184"
class="src rightside">Source</a><a href="#method.to_tokens-15" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-u128" class="section impl">

<a href="../src/quote/to_tokens.rs.html#187-191"
class="src rightside">Source</a><a href="#impl-ToTokens-for-u128" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-16" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#188-190"
class="src rightside">Source</a><a href="#method.to_tokens-16" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-usize" class="section impl">

<a href="../src/quote/to_tokens.rs.html#193-197"
class="src rightside">Source</a><a href="#impl-ToTokens-for-usize" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-17" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#194-196"
class="src rightside">Source</a><a href="#method.to_tokens-17" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-Group" class="section impl">

<a href="../src/quote/to_tokens.rs.html#236-240"
class="src rightside">Source</a><a href="#impl-ToTokens-for-Group" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="../proc_macro2/struct.Group.html" class="struct"
title="struct proc_macro2::Group">Group</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-18" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#237-239"
class="src rightside">Source</a><a href="#method.to_tokens-18" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-Ident" class="section impl">

<a href="../src/quote/to_tokens.rs.html#242-246"
class="src rightside">Source</a><a href="#impl-ToTokens-for-Ident" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="../proc_macro2/struct.Ident.html" class="struct"
title="struct proc_macro2::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-19" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#243-245"
class="src rightside">Source</a><a href="#method.to_tokens-19" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-Literal" class="section impl">

<a href="../src/quote/to_tokens.rs.html#254-258"
class="src rightside">Source</a><a href="#impl-ToTokens-for-Literal" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="../proc_macro2/struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-20" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#255-257"
class="src rightside">Source</a><a href="#method.to_tokens-20" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-Punct" class="section impl">

<a href="../src/quote/to_tokens.rs.html#248-252"
class="src rightside">Source</a><a href="#impl-ToTokens-for-Punct" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="../proc_macro2/struct.Punct.html" class="struct"
title="struct proc_macro2::Punct">Punct</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-21" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#249-251"
class="src rightside">Source</a><a href="#method.to_tokens-21" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-TokenStream" class="section impl">

<a href="../src/quote/to_tokens.rs.html#266-274"
class="src rightside">Source</a><a href="#impl-ToTokens-for-TokenStream" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-22" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#267-269"
class="src rightside">Source</a><a href="#method.to_tokens-22" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

<div id="method.into_token_stream-1" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#271-273"
class="src rightside">Source</a><a href="#method.into_token_stream-1" class="anchor">§</a>

#### fn <a href="#method.into_token_stream" class="fn">into_token_stream</a>(self) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

</div>

<div id="impl-ToTokens-for-CString" class="section impl">

<a href="../src/quote/to_tokens.rs.html#230-234"
class="src rightside">Source</a><a href="#impl-ToTokens-for-CString" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a
href="https://doc.rust-lang.org/1.92.0/alloc/ffi/c_str/struct.CString.html"
class="struct" title="struct alloc::ffi::c_str::CString">CString</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-23" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#231-233"
class="src rightside">Source</a><a href="#method.to_tokens-23" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-String" class="section impl">

<a href="../src/quote/to_tokens.rs.html#121-125"
class="src rightside">Source</a><a href="#impl-ToTokens-for-String" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-24" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#122-124"
class="src rightside">Source</a><a href="#method.to_tokens-24" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-CStr" class="section impl">

<a href="../src/quote/to_tokens.rs.html#224-228"
class="src rightside">Source</a><a href="#impl-ToTokens-for-CStr" class="anchor">§</a>

### impl <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a
href="https://doc.rust-lang.org/1.92.0/core/ffi/c_str/struct.CStr.html"
class="struct" title="struct core::ffi::c_str::CStr">CStr</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-25" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#225-227"
class="src rightside">Source</a><a href="#method.to_tokens-25" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-Cow%3C'a,+T%3E" class="section impl">

<a href="../src/quote/to_tokens.rs.html#89-93"
class="src rightside">Source</a><a href="#impl-ToTokens-for-Cow%3C&#39;a,+T%3E" class="anchor">§</a>

### impl\<'a, T: ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a> + <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html"
class="trait" title="trait alloc::borrow::ToOwned">ToOwned</a> + <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a>\> <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/alloc/borrow/enum.Cow.html"
class="enum" title="enum alloc::borrow::Cow">Cow</a>\<'a, T\>

</div>

<div class="impl-items">

<div id="method.to_tokens-26" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#90-92"
class="src rightside">Source</a><a href="#method.to_tokens-26" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-Option%3CT%3E" class="section impl">

<a href="../src/quote/to_tokens.rs.html#107-113"
class="src rightside">Source</a><a href="#impl-ToTokens-for-Option%3CT%3E" class="anchor">§</a>

### impl\<T: <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a>\> <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

<div class="impl-items">

<div id="method.to_tokens-27" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#108-112"
class="src rightside">Source</a><a href="#method.to_tokens-27" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-%26T" class="section impl">

<a href="../src/quote/to_tokens.rs.html#77-81"
class="src rightside">Source</a><a href="#impl-ToTokens-for-%26T" class="anchor">§</a>

### impl\<T: ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a> + <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a>\> <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-28" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#78-80"
class="src rightside">Source</a><a href="#method.to_tokens-28" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-%26mut+T" class="section impl">

<a href="../src/quote/to_tokens.rs.html#83-87"
class="src rightside">Source</a><a href="#impl-ToTokens-for-%26mut+T" class="anchor">§</a>

### impl\<T: ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a> + <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a>\> <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>

</div>

<div class="impl-items">

<div id="method.to_tokens-29" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#84-86"
class="src rightside">Source</a><a href="#method.to_tokens-29" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-Box%3CT%3E" class="section impl">

<a href="../src/quote/to_tokens.rs.html#95-99"
class="src rightside">Source</a><a href="#impl-ToTokens-for-Box%3CT%3E" class="anchor">§</a>

### impl\<T: ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a> + <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a>\> <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/alloc/boxed/struct.Box.html"
class="struct" title="struct alloc::boxed::Box">Box</a>\<T\>

</div>

<div class="impl-items">

<div id="method.to_tokens-30" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#96-98"
class="src rightside">Source</a><a href="#method.to_tokens-30" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

<div id="impl-ToTokens-for-Rc%3CT%3E" class="section impl">

<a href="../src/quote/to_tokens.rs.html#101-105"
class="src rightside">Source</a><a href="#impl-ToTokens-for-Rc%3CT%3E" class="anchor">§</a>

### impl\<T: ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a> + <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a>\> <a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a> for <a href="https://doc.rust-lang.org/1.92.0/alloc/rc/struct.Rc.html"
class="struct" title="struct alloc::rc::Rc">Rc</a>\<T\>

</div>

<div class="impl-items">

<div id="method.to_tokens-31" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#102-104"
class="src rightside">Source</a><a href="#method.to_tokens-31" class="anchor">§</a>

#### fn <a href="#tymethod.to_tokens" class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
