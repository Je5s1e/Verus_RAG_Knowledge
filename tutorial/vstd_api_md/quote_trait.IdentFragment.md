<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[quote](index.html)

</div>

# Trait <span class="trait">IdentFragment</span> Copy item path

<span class="sub-heading"><a href="../src/quote/ident_fragment.rs.html#14-24"
class="src">Source</a> </span>

</div>

``` rust
pub trait IdentFragment {
    // Required method
    fn fmt(&self, f: &mut Formatter<'_>) -> Result;

    // Provided method
    fn span(&self) -> Option<Span> { ... }
}
```

Expand description

<div class="docblock">

Specialized formatting trait used by `format_ident!`.

[`Ident`](../proc_macro2/struct.Ident.html "struct proc_macro2::Ident")
arguments formatted using this trait will have their `r#` prefix
stripped, if present.

See
[`format_ident!`](macro.format_ident.html "macro quote::format_ident")
for more information.

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.fmt" class="section method">

<a href="../src/quote/ident_fragment.rs.html#16"
class="src rightside">Source</a>

#### fn <a href="#tymethod.fmt" class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

<div class="docblock">

Format this value as an identifier fragment.

</div>

</div>

## Provided Methods<a href="#provided-methods" class="anchor">§</a>

<div class="methods">

<div id="method.span" class="section method">

<a href="../src/quote/ident_fragment.rs.html#21-23"
class="src rightside">Source</a>

#### fn <a href="#method.span" class="fn">span</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>\>

</div>

<div class="docblock">

Span associated with this `IdentFragment`.

If non-`None`, may be inherited by formatted identifiers.

</div>

</div>

## Implementations on Foreign Types<a href="#foreign-impls" class="anchor">§</a>

<div id="impl-IdentFragment-for-bool" class="section impl">

<a href="../src/quote/ident_fragment.rs.html#88"
class="src rightside">Source</a><a href="#impl-IdentFragment-for-bool" class="anchor">§</a>

### impl <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#88"
class="src rightside">Source</a><a href="#method.fmt" class="anchor">§</a>

#### fn <a href="#tymethod.fmt" class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

</div>

<div id="impl-IdentFragment-for-char" class="section impl">

<a href="../src/quote/ident_fragment.rs.html#88"
class="src rightside">Source</a><a href="#impl-IdentFragment-for-char" class="anchor">§</a>

### impl <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div class="impl-items">

<div id="method.fmt-1" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#88"
class="src rightside">Source</a><a href="#method.fmt-1" class="anchor">§</a>

#### fn <a href="#tymethod.fmt" class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

</div>

<div id="impl-IdentFragment-for-str" class="section impl">

<a href="../src/quote/ident_fragment.rs.html#88"
class="src rightside">Source</a><a href="#impl-IdentFragment-for-str" class="anchor">§</a>

### impl <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

<div class="impl-items">

<div id="method.fmt-2" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#88"
class="src rightside">Source</a><a href="#method.fmt-2" class="anchor">§</a>

#### fn <a href="#tymethod.fmt" class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

</div>

<div id="impl-IdentFragment-for-u8" class="section impl">

<a href="../src/quote/ident_fragment.rs.html#89"
class="src rightside">Source</a><a href="#impl-IdentFragment-for-u8" class="anchor">§</a>

### impl <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

<div class="impl-items">

<div id="method.fmt-3" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#89"
class="src rightside">Source</a><a href="#method.fmt-3" class="anchor">§</a>

#### fn <a href="#tymethod.fmt" class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

</div>

<div id="impl-IdentFragment-for-u16" class="section impl">

<a href="../src/quote/ident_fragment.rs.html#89"
class="src rightside">Source</a><a href="#impl-IdentFragment-for-u16" class="anchor">§</a>

### impl <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

<div class="impl-items">

<div id="method.fmt-4" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#89"
class="src rightside">Source</a><a href="#method.fmt-4" class="anchor">§</a>

#### fn <a href="#tymethod.fmt" class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

</div>

<div id="impl-IdentFragment-for-u32" class="section impl">

<a href="../src/quote/ident_fragment.rs.html#89"
class="src rightside">Source</a><a href="#impl-IdentFragment-for-u32" class="anchor">§</a>

### impl <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

<div class="impl-items">

<div id="method.fmt-5" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#89"
class="src rightside">Source</a><a href="#method.fmt-5" class="anchor">§</a>

#### fn <a href="#tymethod.fmt" class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

</div>

<div id="impl-IdentFragment-for-u64" class="section impl">

<a href="../src/quote/ident_fragment.rs.html#89"
class="src rightside">Source</a><a href="#impl-IdentFragment-for-u64" class="anchor">§</a>

### impl <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

<div class="impl-items">

<div id="method.fmt-6" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#89"
class="src rightside">Source</a><a href="#method.fmt-6" class="anchor">§</a>

#### fn <a href="#tymethod.fmt" class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

</div>

<div id="impl-IdentFragment-for-u128" class="section impl">

<a href="../src/quote/ident_fragment.rs.html#89"
class="src rightside">Source</a><a href="#impl-IdentFragment-for-u128" class="anchor">§</a>

### impl <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

<div class="impl-items">

<div id="method.fmt-7" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#89"
class="src rightside">Source</a><a href="#method.fmt-7" class="anchor">§</a>

#### fn <a href="#tymethod.fmt" class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

</div>

<div id="impl-IdentFragment-for-usize" class="section impl">

<a href="../src/quote/ident_fragment.rs.html#89"
class="src rightside">Source</a><a href="#impl-IdentFragment-for-usize" class="anchor">§</a>

### impl <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="impl-items">

<div id="method.fmt-8" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#89"
class="src rightside">Source</a><a href="#method.fmt-8" class="anchor">§</a>

#### fn <a href="#tymethod.fmt" class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

</div>

<div id="impl-IdentFragment-for-Ident" class="section impl">

<a href="../src/quote/ident_fragment.rs.html#46-59"
class="src rightside">Source</a><a href="#impl-IdentFragment-for-Ident" class="anchor">§</a>

### impl <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> for <a href="../proc_macro2/struct.Ident.html" class="struct"
title="struct proc_macro2::Ident">Ident</a>

</div>

<div class="impl-items">

<div id="method.span-1" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#47-49"
class="src rightside">Source</a><a href="#method.span-1" class="anchor">§</a>

#### fn <a href="#method.span" class="fn">span</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>\>

</div>

<div id="method.fmt-9" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#51-58"
class="src rightside">Source</a><a href="#method.fmt-9" class="anchor">§</a>

#### fn <a href="#tymethod.fmt" class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

</div>

<div id="impl-IdentFragment-for-String" class="section impl">

<a href="../src/quote/ident_fragment.rs.html#88"
class="src rightside">Source</a><a href="#impl-IdentFragment-for-String" class="anchor">§</a>

### impl <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> for <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

</div>

<div class="impl-items">

<div id="method.fmt-10" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#88"
class="src rightside">Source</a><a href="#method.fmt-10" class="anchor">§</a>

#### fn <a href="#tymethod.fmt" class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

</div>

<div id="impl-IdentFragment-for-Cow%3C'_,+T%3E" class="section impl">

<a href="../src/quote/ident_fragment.rs.html#61-72"
class="src rightside">Source</a><a href="#impl-IdentFragment-for-Cow%3C&#39;_,+T%3E"
class="anchor">§</a>

### impl\<T\> <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> for <a href="https://doc.rust-lang.org/1.92.0/alloc/borrow/enum.Cow.html"
class="enum" title="enum alloc::borrow::Cow">Cow</a>\<'\_, T\>

<div class="where">

where T: <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> + <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html"
class="trait" title="trait alloc::borrow::ToOwned">ToOwned</a> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.span-2" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#65-67"
class="src rightside">Source</a><a href="#method.span-2" class="anchor">§</a>

#### fn <a href="#method.span" class="fn">span</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>\>

</div>

<div id="method.fmt-11" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#69-71"
class="src rightside">Source</a><a href="#method.fmt-11" class="anchor">§</a>

#### fn <a href="#tymethod.fmt" class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

</div>

<div id="impl-IdentFragment-for-%26T" class="section impl">

<a href="../src/quote/ident_fragment.rs.html#26-34"
class="src rightside">Source</a><a href="#impl-IdentFragment-for-%26T" class="anchor">§</a>

### impl\<T: <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> + ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>\> <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>

</div>

<div class="impl-items">

<div id="method.span-3" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#27-29"
class="src rightside">Source</a><a href="#method.span-3" class="anchor">§</a>

#### fn <a href="#method.span" class="fn">span</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>\>

</div>

<div id="method.fmt-12" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#31-33"
class="src rightside">Source</a><a href="#method.fmt-12" class="anchor">§</a>

#### fn <a href="#tymethod.fmt" class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

</div>

<div id="impl-IdentFragment-for-%26mut+T" class="section impl">

<a href="../src/quote/ident_fragment.rs.html#36-44"
class="src rightside">Source</a><a href="#impl-IdentFragment-for-%26mut+T" class="anchor">§</a>

### impl\<T: <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> + ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>\> <a href="trait.IdentFragment.html" class="trait"
title="trait quote::IdentFragment">IdentFragment</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>

</div>

<div class="impl-items">

<div id="method.span-4" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#37-39"
class="src rightside">Source</a><a href="#method.span-4" class="anchor">§</a>

#### fn <a href="#method.span" class="fn">span</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>\>

</div>

<div id="method.fmt-13" class="section method trait-impl">

<a href="../src/quote/ident_fragment.rs.html#41-43"
class="src rightside">Source</a><a href="#method.fmt-13" class="anchor">§</a>

#### fn <a href="#tymethod.fmt" class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
