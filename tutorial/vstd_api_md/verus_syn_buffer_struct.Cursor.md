<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)::[buffer](index.html)

</div>

# Struct <span class="struct">Cursor</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/buffer.rs.html#97-106"
class="src">Source</a> </span>

</div>

``` rust
pub struct Cursor<'a> { /* private fields */ }
```

Expand description

<div class="docblock">

A cheaply copyable cursor into a `TokenBuffer`.

This cursor holds a shared reference into the immutable data which is
used internally to represent a `TokenStream`, and can be efficiently
manipulated and copied around.

An empty `Cursor` can be created directly, or one may create a
`TokenBuffer` object and get a cursor to its first token with `begin()`.

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-Cursor%3C'a%3E" class="section impl">

<a href="../../src/verus_syn/buffer.rs.html#108-381"
class="src rightside">Source</a><a href="#impl-Cursor%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.empty" class="section method">

<a href="../../src/verus_syn/buffer.rs.html#110-127"
class="src rightside">Source</a>

#### pub fn <a href="#method.empty" class="fn">empty</a>() -\> Self

</div>

<div class="docblock">

Creates a cursor referencing a static empty TokenStream.

</div>

<div id="method.eof" class="section method">

<a href="../../src/verus_syn/buffer.rs.html#183-186"
class="src rightside">Source</a>

#### pub fn <a href="#method.eof" class="fn">eof</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Checks whether the cursor is currently pointing at the end of its valid
scope.

</div>

<div id="method.ident" class="section method">

<a href="../../src/verus_syn/buffer.rs.html#190-196"
class="src rightside">Source</a>

#### pub fn <a href="#method.ident" class="fn">ident</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="../struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>, <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>)\>

</div>

<div class="docblock">

If the cursor is pointing at a `Ident`, returns it along with a cursor
pointing at the next `TokenTree`.

</div>

<div id="method.punct" class="section method">

<a href="../../src/verus_syn/buffer.rs.html#200-208"
class="src rightside">Source</a>

#### pub fn <a href="#method.punct" class="fn">punct</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="../../proc_macro2/struct.Punct.html" class="struct"
title="struct proc_macro2::Punct">Punct</a>, <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>)\>

</div>

<div class="docblock">

If the cursor is pointing at a `Punct`, returns it along with a cursor
pointing at the next `TokenTree`.

</div>

<div id="method.literal" class="section method">

<a href="../../src/verus_syn/buffer.rs.html#212-218"
class="src rightside">Source</a>

#### pub fn <a href="#method.literal" class="fn">literal</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="../../proc_macro2/struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>, <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>)\>

</div>

<div class="docblock">

If the cursor is pointing at a `Literal`, return it along with a cursor
pointing at the next `TokenTree`.

</div>

<div id="method.lifetime" class="section method">

<a href="../../src/verus_syn/buffer.rs.html#222-236"
class="src rightside">Source</a>

#### pub fn <a href="#method.lifetime" class="fn">lifetime</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="../struct.Lifetime.html" class="struct"
title="struct verus_syn::Lifetime">Lifetime</a>, <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>)\>

</div>

<div class="docblock">

If the cursor is pointing at a `Lifetime`, returns it along with a
cursor pointing at the next `TokenTree`.

</div>

<div id="method.group" class="section method">

<a href="../../src/verus_syn/buffer.rs.html#240-259"
class="src rightside">Source</a>

#### pub fn <a href="#method.group" class="fn">group</a>( self, delim: <a href="../../proc_macro2/enum.Delimiter.html" class="enum"
title="enum proc_macro2::Delimiter">Delimiter</a>, ) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>, <a href="../../proc_macro2/extra/struct.DelimSpan.html" class="struct"
title="struct proc_macro2::extra::DelimSpan">DelimSpan</a>, <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>)\>

</div>

<div class="docblock">

If the cursor is pointing at a `Group` with the given delimiter, returns
a cursor into that group and one pointing to the next `TokenTree`.

</div>

<div id="method.any_group" class="section method">

<a href="../../src/verus_syn/buffer.rs.html#263-274"
class="src rightside">Source</a>

#### pub fn <a href="#method.any_group" class="fn">any_group</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>, <a href="../../proc_macro2/enum.Delimiter.html" class="enum"
title="enum proc_macro2::Delimiter">Delimiter</a>, <a href="../../proc_macro2/extra/struct.DelimSpan.html" class="struct"
title="struct proc_macro2::extra::DelimSpan">DelimSpan</a>, <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>)\>

</div>

<div class="docblock">

If the cursor is pointing at a `Group`, returns a cursor into the group
and one pointing to the next `TokenTree`.

</div>

<div id="method.token_stream" class="section method">

<a href="../../src/verus_syn/buffer.rs.html#288-296"
class="src rightside">Source</a>

#### pub fn <a href="#method.token_stream" class="fn">token_stream</a>(self) -\> <a href="../../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="docblock">

Copies all remaining tokens visible from this cursor into a
`TokenStream`.

</div>

<div id="method.token_tree" class="section method">

<a href="../../src/verus_syn/buffer.rs.html#305-316"
class="src rightside">Source</a>

#### pub fn <a href="#method.token_tree" class="fn">token_tree</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="../../proc_macro2/enum.TokenTree.html" class="enum"
title="enum proc_macro2::TokenTree">TokenTree</a>, <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>)\>

</div>

<div class="docblock">

If the cursor is pointing at a `TokenTree`, returns it along with a
cursor pointing at the next `TokenTree`.

Returns `None` if the cursor has reached the end of its stream.

This method does not treat `None`-delimited groups as transparent, and
will return a `Group(None, ..)` if the cursor is looking at one.

</div>

<div id="method.span" class="section method">

<a href="../../src/verus_syn/buffer.rs.html#320-335"
class="src rightside">Source</a>

#### pub fn <a href="#method.span" class="fn">span</a>(self) -\> <a href="../../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="docblock">

Returns the `Span` of the current token, or `Span::call_site()` if this
cursor points to eof.

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-Cursor%3C'a%3E" class="section impl">

<a href="../../src/verus_syn/buffer.rs.html#385-389"
class="src rightside">Source</a><a href="#impl-Clone-for-Cursor%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../../src/verus_syn/buffer.rs.html#386-388"
class="src rightside">Source</a><a href="#method.clone" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone"
class="fn">clone</a>(&self) -\> Self

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

<div id="impl-PartialEq-for-Cursor%3C'a%3E" class="section impl">

<a href="../../src/verus_syn/buffer.rs.html#393-397"
class="src rightside">Source</a><a href="#impl-PartialEq-for-Cursor%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a> for <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.eq" class="section method trait-impl">

<a href="../../src/verus_syn/buffer.rs.html#394-396"
class="src rightside">Source</a><a href="#method.eq" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#tymethod.eq"
class="fn">eq</a>(&self, other: &Self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
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

<div id="impl-PartialOrd-for-Cursor%3C'a%3E" class="section impl">

<a href="../../src/verus_syn/buffer.rs.html#399-407"
class="src rightside">Source</a><a href="#impl-PartialOrd-for-Cursor%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html"
class="trait" title="trait core::cmp::PartialOrd">PartialOrd</a> for <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>

</div>

<div class="impl-items">

<div id="method.partial_cmp" class="section method trait-impl">

<a href="../../src/verus_syn/buffer.rs.html#400-406"
class="src rightside">Source</a><a href="#method.partial_cmp" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#tymethod.partial_cmp"
class="fn">partial_cmp</a>(&self, other: &Self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>\>

</div>

<div class="docblock">

This method returns an ordering between `self` and `other` values if one
exists. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

</div>

<div id="method.lt" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1398"
class="src">Source</a></span><a href="#method.lt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.lt"
class="fn">lt</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests less than (for `self` and `other`) and is used by the `<`
operator. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.lt)

</div>

<div id="method.le" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1416"
class="src">Source</a></span><a href="#method.le" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.le"
class="fn">le</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests less than or equal to (for `self` and `other`) and is used by the
`<=` operator. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.le)

</div>

<div id="method.gt" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1434"
class="src">Source</a></span><a href="#method.gt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.gt"
class="fn">gt</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests greater than (for `self` and `other`) and is used by the `>`
operator. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.gt)

</div>

<div id="method.ge" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1452"
class="src">Source</a></span><a href="#method.ge" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.ge"
class="fn">ge</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests greater than or equal to (for `self` and `other`) and is used by
the `>=` operator. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.ge)

</div>

</div>

<div id="impl-Copy-for-Cursor%3C'a%3E" class="section impl">

<a href="../../src/verus_syn/buffer.rs.html#383"
class="src rightside">Source</a><a href="#impl-Copy-for-Cursor%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a> for <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>

</div>

<div id="impl-Eq-for-Cursor%3C'a%3E" class="section impl">

<a href="../../src/verus_syn/buffer.rs.html#391"
class="src rightside">Source</a><a href="#impl-Eq-for-Cursor%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> for <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-Cursor%3C'a%3E" class="section impl">

<a href="#impl-Freeze-for-Cursor%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>

</div>

<div id="impl-RefUnwindSafe-for-Cursor%3C'a%3E" class="section impl">

<a href="#impl-RefUnwindSafe-for-Cursor%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>

</div>

<div id="impl-Send-for-Cursor%3C'a%3E" class="section impl">

<a href="#impl-Send-for-Cursor%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>

</div>

<div id="impl-Sync-for-Cursor%3C'a%3E" class="section impl">

<a href="#impl-Sync-for-Cursor%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>

</div>

<div id="impl-Unpin-for-Cursor%3C'a%3E" class="section impl">

<a href="#impl-Unpin-for-Cursor%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>

</div>

<div id="impl-UnwindSafe-for-Cursor%3C'a%3E" class="section impl">

<a href="#impl-UnwindSafe-for-Cursor%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>\<'a\>

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
