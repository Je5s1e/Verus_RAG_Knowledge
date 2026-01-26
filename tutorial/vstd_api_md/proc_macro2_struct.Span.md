<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[proc_macro2](index.html)

</div>

# Struct <span class="struct">Span</span> Copy item path

<span class="sub-heading"><a href="../src/proc_macro2/lib.rs.html#390-393" class="src">Source</a>
</span>

</div>

``` rust
pub struct Span { /* private fields */ }
```

Expand description

<div class="docblock">

A region of source code, along with macro expansion information.

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-Span" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#395-567"
class="src rightside">Source</a><a href="#impl-Span" class="anchor">§</a>

### impl <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="impl-items">

<div id="method.call_site" class="section method">

<a href="../src/proc_macro2/lib.rs.html#415-417"
class="src rightside">Source</a>

#### pub fn <a href="#method.call_site" class="fn">call_site</a>() -\> Self

</div>

<div class="docblock">

The span of the invocation of the current procedural macro.

Identifiers created with this span will be resolved as if they were
written directly at the macro call location (call-site hygiene) and
other code at the macro call site will be able to refer to them as well.

</div>

<div id="method.mixed_site" class="section method">

<a href="../src/proc_macro2/lib.rs.html#422-424"
class="src rightside">Source</a>

#### pub fn <a href="#method.mixed_site" class="fn">mixed_site</a>() -\> Self

</div>

<div class="docblock">

The span located at the invocation of the procedural macro, but with
local variables, labels, and `$crate` resolved at the definition site of
the macro. This is the same hygiene behavior as `macro_rules`.

</div>

<div id="method.resolved_at" class="section method">

<a href="../src/proc_macro2/lib.rs.html#437-439"
class="src rightside">Source</a>

#### pub fn <a href="#method.resolved_at" class="fn">resolved_at</a>(&self, other: <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>) -\> <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="docblock">

Creates a new span with the same line/column information as `self` but
that resolves symbols as though it were at `other`.

</div>

<div id="method.located_at" class="section method">

<a href="../src/proc_macro2/lib.rs.html#443-445"
class="src rightside">Source</a>

#### pub fn <a href="#method.located_at" class="fn">located_at</a>(&self, other: <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>) -\> <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="docblock">

Creates a new span with the same name resolution behavior as `self` but
with the line/column information of `other`.

</div>

<div id="method.unwrap" class="section method">

<a href="../src/proc_macro2/lib.rs.html#458-460"
class="src rightside">Source</a>

#### pub fn <a href="#method.unwrap" class="fn">unwrap</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/proc_macro/struct.Span.html"
class="struct" title="struct proc_macro::Span">Span</a>

</div>

<div class="docblock">

Convert `proc_macro2::Span` to `proc_macro::Span`.

This method is available when building with a nightly compiler, or when
building with rustc 1.29+ *without* semver exempt features.

##### <a href="#panics" class="doc-anchor">§</a>Panics

Panics if called from outside of a procedural macro. Unlike
`proc_macro2::Span`, the `proc_macro::Span` type can only exist within
the context of a procedural macro invocation.

</div>

<div id="method.byte_range" class="section method">

<a href="../src/proc_macro2/lib.rs.html#480-482"
class="src rightside">Source</a>

#### pub fn <a href="#method.byte_range" class="fn">byte_range</a>(&self) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/ops/range/struct.Range.html"
class="struct" title="struct core::ops::range::Range">Range</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\>

</div>

<div class="docblock">

Returns the span’s byte position range in the source file.

This method requires the `"span-locations"` feature to be enabled.

When executing in a procedural macro context, the returned range is only
accurate if compiled with a nightly toolchain. The stable toolchain does
not have this information available. When executing outside of a
procedural macro, such as main.rs or build.rs, the byte range is always
accurate regardless of toolchain.

</div>

<div id="method.start" class="section method">

<a href="../src/proc_macro2/lib.rs.html#495-497"
class="src rightside">Source</a>

#### pub fn <a href="#method.start" class="fn">start</a>(&self) -\> <a href="struct.LineColumn.html" class="struct"
title="struct proc_macro2::LineColumn">LineColumn</a>

</div>

<div class="docblock">

Get the starting line/column in the source file for this span.

This method requires the `"span-locations"` feature to be enabled.

When executing in a procedural macro context, the returned line/column
are only meaningful if compiled with a nightly toolchain. The stable
toolchain does not have this information available. When executing
outside of a procedural macro, such as main.rs or build.rs, the
line/column are always meaningful regardless of toolchain.

</div>

<div id="method.end" class="section method">

<a href="../src/proc_macro2/lib.rs.html#510-512"
class="src rightside">Source</a>

#### pub fn <a href="#method.end" class="fn">end</a>(&self) -\> <a href="struct.LineColumn.html" class="struct"
title="struct proc_macro2::LineColumn">LineColumn</a>

</div>

<div class="docblock">

Get the ending line/column in the source file for this span.

This method requires the `"span-locations"` feature to be enabled.

When executing in a procedural macro context, the returned line/column
are only meaningful if compiled with a nightly toolchain. The stable
toolchain does not have this information available. When executing
outside of a procedural macro, such as main.rs or build.rs, the
line/column are always meaningful regardless of toolchain.

</div>

<div id="method.file" class="section method">

<a href="../src/proc_macro2/lib.rs.html#521-523"
class="src rightside">Source</a>

#### pub fn <a href="#method.file" class="fn">file</a>(&self) -\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

</div>

<div class="docblock">

The path to the source file in which this span occurs, for display
purposes.

This might not correspond to a valid file system path. It might be
remapped, or might be an artificial path such as `"<macro expansion>"`.

</div>

<div id="method.local_file" class="section method">

<a href="../src/proc_macro2/lib.rs.html#533-535"
class="src rightside">Source</a>

#### pub fn <a href="#method.local_file" class="fn">local_file</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/path/struct.PathBuf.html"
class="struct" title="struct std::path::PathBuf">PathBuf</a>\>

</div>

<div class="docblock">

The path to the source file in which this span occurs on disk.

This is the actual path on disk. It is unaffected by path remapping.

This path should not be embedded in the output of the macro; prefer
`file()` instead.

</div>

<div id="method.join" class="section method">

<a href="../src/proc_macro2/lib.rs.html#544-546"
class="src rightside">Source</a>

#### pub fn <a href="#method.join" class="fn">join</a>(&self, other: <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>\>

</div>

<div class="docblock">

Create a new span encompassing `self` and `other`.

Returns `None` if `self` and `other` are from different files.

Warning: the underlying
[`proc_macro::Span::join`](https://doc.rust-lang.org/1.92.0/proc_macro/struct.Span.html#method.join "method proc_macro::Span::join")
method is nightly-only. When called from within a procedural macro not
using a nightly compiler, this method will always return `None`.

</div>

<div id="method.source_text" class="section method">

<a href="../src/proc_macro2/lib.rs.html#564-566"
class="src rightside">Source</a>

#### pub fn <a href="#method.source_text" class="fn">source_text</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>\>

</div>

<div class="docblock">

Returns the source text behind a span. This preserves the original
source code, including spaces and comments. It only returns a result if
the span corresponds to real source code.

Note: The observable result of a macro should only rely on the tokens
and not on this source text. The result of this function is a best
effort to be used for diagnostics only.

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-Span" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#389"
class="src rightside">Source</a><a href="#impl-Clone-for-Span" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#389"
class="src rightside">Source</a><a href="#method.clone" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone"
class="fn">clone</a>(&self) -\> <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

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

<div id="impl-Debug-for-Span" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#570-574"
class="src rightside">Source</a><a href="#impl-Debug-for-Span" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

<div class="docblock">

Prints a span in a form convenient for debugging.

</div>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#571-573"
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

<div id="impl-From%3CSpan%3E-for-Span" class="section impl">

<a href="../src/proc_macro2/wrapper.rs.html#531-535"
class="src rightside">Source</a><a href="#impl-From%3CSpan%3E-for-Span" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="https://doc.rust-lang.org/1.92.0/proc_macro/struct.Span.html"
class="struct" title="struct proc_macro::Span">Span</a>\> for <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a href="../src/proc_macro2/wrapper.rs.html#532-534"
class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(proc_span: <a href="https://doc.rust-lang.org/1.92.0/proc_macro/struct.Span.html"
class="struct" title="struct proc_macro::Span">Span</a>) -\> Self

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-Copy-for-Span" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#389"
class="src rightside">Source</a><a href="#impl-Copy-for-Span" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a> for <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-Span" class="section impl">

<a href="#impl-Freeze-for-Span" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div id="impl-RefUnwindSafe-for-Span" class="section impl">

<a href="#impl-RefUnwindSafe-for-Span" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div id="impl-Send-for-Span" class="section impl">

<a href="#impl-Send-for-Span" class="anchor">§</a>

### impl \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div id="impl-Sync-for-Span" class="section impl">

<a href="#impl-Sync-for-Span" class="anchor">§</a>

### impl \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div id="impl-Unpin-for-Span" class="section impl">

<a href="#impl-Unpin-for-Span" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div id="impl-UnwindSafe-for-Span" class="section impl">

<a href="#impl-UnwindSafe-for-Span" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

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

<div id="method.from-1" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#788"
class="src rightside">Source</a><a href="#method.from-1" class="anchor">§</a>

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
