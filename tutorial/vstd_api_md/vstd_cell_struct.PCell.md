<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[cell](index.html)

</div>

# Struct <span class="struct">PCell</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/cell.rs.html#59-61" class="src">Source</a>
</span>

</div>

``` rust
pub struct PCell<V> { /* private fields */ }
```

Expand description

<div class="docblock">

`PCell<V>` (which stands for “permissioned call”) is the primitive Verus
`Cell` type.

Technically, it is a wrapper around
`core::cell::UnsafeCell<core::mem::MaybeUninit<V>>`, and thus has the
same runtime properties: there are no runtime checks (as there would be
for Rust’s traditional
[`core::cell::RefCell`](https://doc.rust-lang.org/core/cell/struct.RefCell.html)).
Its data may be uninitialized.

Furthermore (and unlike both
[`core::cell::Cell`](https://doc.rust-lang.org/core/cell/struct.Cell.html)
and
[`core::cell::RefCell`](https://doc.rust-lang.org/core/cell/struct.RefCell.html)),
a `PCell<V>` may be `Sync` (depending on `V`). Thanks to verification,
Verus ensures that access to the cell is data-race-free.

`PCell` uses a *ghost permission token* similar to
[`simple_pptr::PPtr`](../simple_pptr/struct.PPtr.html "struct vstd::simple_pptr::PPtr")
– see the
[`simple_pptr::PPtr`](../simple_pptr/struct.PPtr.html "struct vstd::simple_pptr::PPtr")
documentation for the basics. For `PCell`, the associated type of the
permission token is
[`cell::PointsTo`](struct.PointsTo.html "struct vstd::cell::PointsTo").

#### <a href="#differences-from-pptr" class="doc-anchor">§</a>Differences from `PPtr`.

The key difference is that, whereas
[`simple_pptr::PPtr`](../simple_pptr/struct.PPtr.html "struct vstd::simple_pptr::PPtr")
represents a fixed address in memory, a `PCell` has *no* fixed address
because a `PCell` might be moved. As such, the [`pcell.id()`](PCell::id)
does not correspond to a memory address; rather, it is a unique
identifier that is fixed for a given cell, even when it is moved.

The arbitrary ID given by [`pcell.id()`](PCell::id) is of type
[`CellId`](struct.CellId.html "struct vstd::cell::CellId"). Despite the
fact that it is, in some ways, “like a pointer”, note that `CellId` does
not support any meangingful arithmetic, has no concept of a “null ID”,
and has no runtime representation.

Also note that the `PCell` might be dropped before the `PointsTo` token
is dropped, although in that case it will no longer be possible to use
the `PointsTo` in `exec` code to extract data from the cell.

#### <a href="#example-todo" class="doc-anchor">§</a>Example (TODO)

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-PCell%3CV%3E" class="section impl">

<a href="../../src/vstd/cell.rs.html#154-277"
class="src rightside">Source</a><a href="#impl-PCell%3CV%3E" class="anchor">§</a>

### impl\<V\> <a href="struct.PCell.html" class="struct"
title="struct vstd::cell::PCell">PCell</a>\<V\>

</div>

<div class="impl-items">

<div id="method.empty" class="section method">

<a href="../../src/vstd/cell.rs.html#161-167"
class="src rightside">Source</a>

#### pub const fn <a href="#method.empty" class="fn">empty</a>() -\> (<a href="struct.PCell.html" class="struct"
title="struct vstd::cell::PCell">PCell</a>\<V\>, <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<<a href="struct.PointsTo.html" class="struct"
title="struct vstd::cell::PointsTo">PointsTo</a>\<V\>\>)

</div>

<div class="docblock">

Return an empty (“uninitialized”) cell.

</div>

<div id="method.new" class="section method">

<a href="../../src/vstd/cell.rs.html#171-177"
class="src rightside">Source</a>

#### pub const fn <a href="#method.new" class="fn">new</a>(v: V) -\> (<a href="struct.PCell.html" class="struct"
title="struct vstd::cell::PCell">PCell</a>\<V\>, <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<<a href="struct.PointsTo.html" class="struct"
title="struct vstd::cell::PointsTo">PointsTo</a>\<V\>\>)

</div>

<div id="method.put" class="section method">

<a href="../../src/vstd/cell.rs.html#181-192"
class="src rightside">Source</a>

#### pub fn <a href="#method.put" class="fn">put</a>(&self, verus_tmp_perm: <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<&mut <a href="struct.PointsTo.html" class="struct"
title="struct vstd::cell::PointsTo">PointsTo</a>\<V\>\>, v: V)

</div>

<div id="method.take" class="section method">

<a href="../../src/vstd/cell.rs.html#196-212"
class="src rightside">Source</a>

#### pub fn <a href="#method.take" class="fn">take</a>(&self, verus_tmp_perm: <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<&mut <a href="struct.PointsTo.html" class="struct"
title="struct vstd::cell::PointsTo">PointsTo</a>\<V\>\>) -\> V

</div>

<div id="method.replace" class="section method">

<a href="../../src/vstd/cell.rs.html#216-232"
class="src rightside">Source</a>

#### pub fn <a href="#method.replace" class="fn">replace</a>(&self, verus_tmp_perm: <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<&mut <a href="struct.PointsTo.html" class="struct"
title="struct vstd::cell::PointsTo">PointsTo</a>\<V\>\>, in_v: V) -\> V

</div>

<div id="method.borrow" class="section method">

<a href="../../src/vstd/cell.rs.html#239-249"
class="src rightside">Source</a>

#### pub fn <a href="#method.borrow" class="fn">borrow</a>\<'a\>(&'a self, verus_tmp_perm: <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<&'a <a href="struct.PointsTo.html" class="struct"
title="struct vstd::cell::PointsTo">PointsTo</a>\<V\>\>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a V</a>

</div>

<div id="method.into_inner" class="section method">

<a href="../../src/vstd/cell.rs.html#254-265"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_inner" class="fn">into_inner</a>(self, verus_tmp_perm: <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<<a href="struct.PointsTo.html" class="struct"
title="struct vstd::cell::PointsTo">PointsTo</a>\<V\>\>) -\> V

</div>

</div>

<div id="impl-PCell%3CV%3E-1" class="section impl">

<a href="../../src/vstd/cell.rs.html#279-294"
class="src rightside">Source</a><a href="#impl-PCell%3CV%3E-1" class="anchor">§</a>

### impl\<V: <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a>\> <a href="struct.PCell.html" class="struct"
title="struct vstd::cell::PCell">PCell</a>\<V\>

</div>

<div class="impl-items">

<div id="method.write" class="section method">

<a href="../../src/vstd/cell.rs.html#282-293"
class="src rightside">Source</a>

#### pub fn <a href="#method.write" class="fn">write</a>(&self, verus_tmp_perm: <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<&mut <a href="struct.PointsTo.html" class="struct"
title="struct vstd::cell::PointsTo">PointsTo</a>\<V\>\>, in_v: V)

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Send-for-PCell%3CT%3E" class="section impl">

<a href="../../src/vstd/cell.rs.html#71-73"
class="src rightside">Source</a><a href="#impl-Send-for-PCell%3CT%3E" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.PCell.html" class="struct"
title="struct vstd::cell::PCell">PCell</a>\<T\>

</div>

<div id="impl-Sync-for-PCell%3CT%3E" class="section impl">

<a href="../../src/vstd/cell.rs.html#66-68"
class="src rightside">Source</a><a href="#impl-Sync-for-PCell%3CT%3E" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.PCell.html" class="struct"
title="struct vstd::cell::PCell">PCell</a>\<T\>

<div class="docblock">

`PCell` is *always* safe to `Send` or `Sync`. Rather, it is the
[`PointsTo`](struct.PointsTo.html "struct vstd::cell::PointsTo") object
where `Send` and `Sync` matter. (It doesn’t matter if you move the bytes
to another thread if you can’t access them.)

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-PCell%3CV%3E" class="section impl">

<a href="#impl-Freeze-for-PCell%3CV%3E" class="anchor">§</a>

### impl\<V\> \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.PCell.html" class="struct"
title="struct vstd::cell::PCell">PCell</a>\<V\>

</div>

<div id="impl-RefUnwindSafe-for-PCell%3CV%3E" class="section impl">

<a href="#impl-RefUnwindSafe-for-PCell%3CV%3E" class="anchor">§</a>

### impl\<V\> \!<a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.PCell.html" class="struct"
title="struct vstd::cell::PCell">PCell</a>\<V\>

</div>

<div id="impl-Unpin-for-PCell%3CV%3E" class="section impl">

<a href="#impl-Unpin-for-PCell%3CV%3E" class="anchor">§</a>

### impl\<V\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.PCell.html" class="struct"
title="struct vstd::cell::PCell">PCell</a>\<V\>

<div class="where">

where V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>,

</div>

</div>

<div id="impl-UnwindSafe-for-PCell%3CV%3E" class="section impl">

<a href="#impl-UnwindSafe-for-PCell%3CV%3E" class="anchor">§</a>

### impl\<V\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.PCell.html" class="struct"
title="struct vstd::cell::PCell">PCell</a>\<V\>

<div class="where">

where V: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a>,

</div>

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

<div id="method.borrow-1" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#214"
class="src rightside">Source</a><a href="#method.borrow-1" class="anchor">§</a>

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
