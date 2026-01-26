<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[simple_pptr](index.html)

</div>

# Struct <span class="struct">PPtr</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/simple_pptr.rs.html#153" class="src">Source</a>
</span>

</div>

``` rust
pub struct PPtr<V>(pub usize, pub PhantomData<V>);
```

Expand description

<div class="docblock">

`PPtr` (which stands for “permissioned pointer”) is a wrapper around a
raw pointer to a heap-allocated `V`. This is designed to be simpler to
use that Verus’s [more general pointer
support](../raw_ptr/index.html "mod vstd::raw_ptr"), but also to serve
as a better introductory point. Historically, `PPtr` was positioned as a
“trusted primitive” of Verus, but now, it is implemented and verified
from the more general pointer support, which operates on similar
principles, but which is much precise to Rust’s pointer semantics.

A `PPtr` is equvialent to its `usize`-based address. The type paramter
`V` technically doesn’t matter, and you can freely convert between
`PPtr<V>` and `PPtr<W>` by casting to and from the `usize` address. What
*really* matters is the type paramter of the `PointsTo<V>`.

In order to access (read or write) the value behind the pointer, the
user needs a special *ghost permission token*,
[`PointsTo<V>`](struct.PointsTo.html "struct vstd::simple_pptr::PointsTo").
This object is `tracked`, which means that it is “only a proof
construct” that does not appear in compiled code, but its uses *are*
checked by the borrow-checker. This ensures memory safety,
data-race-freedom, prohibits use-after-free, etc.

#### <a href="#pointsto-objects" class="doc-anchor">§</a>PointsTo objects.

The
[`PointsTo`](struct.PointsTo.html "struct vstd::simple_pptr::PointsTo")
object represents both the ability to access (read or write) the data
behind the pointer *and* the ability to free it (return it to the memory
allocator).

The `perm: PointsTo<V>` object tracks two pieces of data:

- [`perm.pptr()`](PointsTo::pptr) is the pointer that the permission is
  associated to.
- [`perm.mem_contents()`](PointsTo::mem_contents) is the memory
  contents, which is one of either:
  - [`MemContents::Uninit`](../raw_ptr/enum.MemContents.html#variant.Uninit "variant vstd::raw_ptr::MemContents::Uninit")
    if the memory pointed-to by by the pointer is uninitialized.
  - [`MemContents::Init(v)`](../raw_ptr/enum.MemContents.html#variant.Init "variant vstd::raw_ptr::MemContents::Init")
    if the memory points-to the the value `v`.

Your access to the `PointsTo` object determines what operations you can
safely perform with the pointer:

- You can *read* from the pointer as long as you have read access to the
  `PointsTo` object, e.g., `&PointsTo<V>`.
- You can *write* to the pointer as long as you have mutable access to
  the `PointsTo` object, e.g., `&mut PointsTo<V>`
- You can call `free` to deallocate the memory as long as you have full
  onwership of the `PointsTo` object (i.e., the ability to move it).

For those familiar with separation logic, the `PointsTo` object plays a
role similar to that of the “points-to” operator, *ptr* ↦ *value*.

#### <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
fn main() {
    unsafe {
        // ALLOCATE
        // p: PPtr<u64>, points_to: PointsTo<u64>
        let (p, Tracked(mut points_to)) = PPtr::<u64>::empty();

        assert(points_to.mem_contents() === MemContents::Uninit);
        assert(points_to.pptr() == p);

        // unsafe { *p = 5; }
        p.write(Tracked(&mut points_to), 5);

        assert(points_to.mem_contents() === MemContents::Init(5));
        assert(points_to.pptr() == p);

        // let x = unsafe { *p };
        let x = p.read(Tracked(&points_to));

        assert(x == 5);

        // DEALLOCATE
        let y = p.into_inner(Tracked(points_to));

        assert(y == 5);
    }
}
```

</div>

#### <a href="#examples-of-incorrect-usage" class="doc-anchor">§</a>Examples of incorrect usage

The following code has a use-after-free bug, and it is rejected by Verus
because it fails to satisfy Rust’s ownership-checker.

<div class="example-wrap">

``` rust
fn main() {
    unsafe {
        // ALLOCATE
        // p: PPtr<u64>, points_to: PointsTo<u64>
        let (p, Tracked(mut points_to)) = PPtr::<u64>::empty();

        // unsafe { *p = 5; }
        p.write(Tracked(&mut points_to), 5);

        // let x = unsafe { *p };
        let x = p.read(Tracked(&points_to));

        // DEALLOCATE
        p.free(Tracked(points_to));                 // `points_to` is moved here

        // READ-AFTER-FREE
        let x2 = p.read(Tracked(&mut points_to));   // so it can't be used here
    }
}
```

</div>

The following doesn’t violate Rust’s ownership-checking, but it “mixes
up” the `PointsTo` objects, attempting to use the wrong `PointsTo` for
the given pointer. This violates the precondition on
[`p.read()`](struct.PPtr.html#method.read "method vstd::simple_pptr::PPtr::read").

<div class="example-wrap">

``` rust
fn main() {
    unsafe {
        // ALLOCATE p
        let (p, Tracked(mut perm_p)) = PPtr::<u64>::empty();

        // ALLOCATE q
        let (q, Tracked(mut perm_q)) = PPtr::<u64>::empty();

        // DEALLOCATE p
        p.free(Tracked(perm_p));

        // READ-AFTER-FREE (read from p, try to use q's permission object)
        let x = p.read(Tracked(&mut perm_q));
    }
}
```

</div>

#### <a href="#differences-from-pcell" class="doc-anchor">§</a>Differences from `PCell`.

`PPtr` is similar to
[`cell::PCell`](../cell/struct.PCell.html "struct vstd::cell::PCell"),
but has a few key differences:

- In `PCell<V>`, the type `V` is placed internally to the `PCell`,
  whereas with `PPtr`, the type `V` is placed at some location on the
  heap.
- Since `PPtr` is just a pointer (represented by an integer), it can be
  `Copy`.
- The `ptr::PointsTo` token represents not just the permission to
  read/write the contents, but also to deallocate.

#### <a href="#simplifications-relative-to-more-general-pointer-api"
class="doc-anchor">§</a>Simplifications relative to more general pointer API

- Pointers are only represented by addresses and don’t have a general
  notion of provenance
- Pointers are untyped (only `PointsTo` is typed).
- The `PointsTo` also encapsulates the permission to free a pointer.
- `PointsTo` tokens are non-fungible. They can’t be broken up or made
  variable-sized.

</div>

## Tuple Fields<a href="#fields" class="anchor">§</a>

<span id="structfield.0"
class="structfield section-header"><a href="#structfield.0" class="anchor field">§</a>`0: `<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive"><code>usize</code></a></span><span id="structfield.1"
class="structfield section-header"><a href="#structfield.1" class="anchor field">§</a>`1: `<a
href="https://doc.rust-lang.org/1.92.0/core/marker/struct.PhantomData.html"
class="struct"
title="struct core::marker::PhantomData"><code>PhantomData</code></a>`<V>`</span>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-PPtr%3CV%3E" class="section impl">

<a href="../../src/vstd/simple_pptr.rs.html#174-218"
class="src rightside">Source</a><a href="#impl-PPtr%3CV%3E" class="anchor">§</a>

### impl\<V\> <a href="struct.PPtr.html" class="struct"
title="struct vstd::simple_pptr::PPtr">PPtr</a>\<V\>

</div>

<div class="impl-items">

<div id="method.addr" class="section method">

<a href="../../src/vstd/simple_pptr.rs.html#184-189"
class="src rightside">Source</a>

#### pub fn <a href="#method.addr" class="fn">addr</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Cast a pointer to an integer.

</div>

<div id="method.from_addr" class="section method">

<a href="../../src/vstd/simple_pptr.rs.html#203-208"
class="src rightside">Source</a>

#### pub fn <a href="#method.from_addr" class="fn">from_addr</a>(u: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> Self

</div>

<div class="docblock">

Cast an integer to a pointer.

Note that this does *not* require or ensure that the pointer is valid.
Of course, if the user creates an invalid pointer, they would still not
be able to create a valid
[`PointsTo`](struct.PointsTo.html "struct vstd::simple_pptr::PointsTo")
token for it, and thus they would never be able to access the data
behind the pointer.

This is analogous to normal Rust, where casting to a pointer is always
possible, but dereferencing a pointer is an `unsafe` operation. With
PPtr, casting to a pointer is likewise always possible, while
dereferencing it is only allowed when the right preconditions are met.

</div>

</div>

<div id="impl-PPtr%3CV%3E-1" class="section impl">

<a href="../../src/vstd/simple_pptr.rs.html#335-555"
class="src rightside">Source</a><a href="#impl-PPtr%3CV%3E-1" class="anchor">§</a>

### impl\<V\> <a href="struct.PPtr.html" class="struct"
title="struct vstd::simple_pptr::PPtr">PPtr</a>\<V\>

</div>

<div class="impl-items">

<div id="method.empty" class="section method">

<a href="../../src/vstd/simple_pptr.rs.html#338-372"
class="src rightside">Source</a>

#### pub fn <a href="#method.empty" class="fn">empty</a>() -\> (<a href="struct.PPtr.html" class="struct"
title="struct vstd::simple_pptr::PPtr">PPtr</a>\<V\>, <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<<a href="struct.PointsTo.html" class="struct"
title="struct vstd::simple_pptr::PointsTo">PointsTo</a>\<V\>\>)

</div>

<div class="docblock">

Allocates heap memory for type `V`, leaving it uninitialized.

</div>

<div id="method.new" class="section method">

<a href="../../src/vstd/simple_pptr.rs.html#377-386"
class="src rightside">Source</a>

#### pub fn <a href="#method.new" class="fn">new</a>(v: V) -\> (<a href="struct.PPtr.html" class="struct"
title="struct vstd::simple_pptr::PPtr">PPtr</a>\<V\>, <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<<a href="struct.PointsTo.html" class="struct"
title="struct vstd::simple_pptr::PointsTo">PointsTo</a>\<V\>\>)

</div>

<div class="docblock">

Allocates heap memory for type `V`, leaving it initialized with the
given value `v`.

</div>

<div id="method.free" class="section method">

<a href="../../src/vstd/simple_pptr.rs.html#393-414"
class="src rightside">Source</a>

#### pub fn <a href="#method.free" class="fn">free</a>(self, verus_tmp_perm: <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<<a href="struct.PointsTo.html" class="struct"
title="struct vstd::simple_pptr::PointsTo">PointsTo</a>\<V\>\>)

</div>

<div class="docblock">

Free the memory pointed to be `perm`. Requires the memory to be
uninitialized.

This consumes `perm`, since it will no longer be safe to access that
memory location.

</div>

<div id="method.into_inner" class="section method">

<a href="../../src/vstd/simple_pptr.rs.html#422-434"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_inner" class="fn">into_inner</a>(self, verus_tmp_perm: <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<<a href="struct.PointsTo.html" class="struct"
title="struct vstd::simple_pptr::PointsTo">PointsTo</a>\<V\>\>) -\> V

</div>

<div class="docblock">

Free the memory pointed to be `perm` and return the value that was
previously there. Requires the memory to be initialized. This consumes
the
[`PointsTo`](struct.PointsTo.html "struct vstd::simple_pptr::PointsTo")
token, since the user is giving up access to the memory by freeing it.

</div>

<div id="method.put" class="section method">

<a href="../../src/vstd/simple_pptr.rs.html#442-457"
class="src rightside">Source</a>

#### pub fn <a href="#method.put" class="fn">put</a>(self, verus_tmp_perm: <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<&mut <a href="struct.PointsTo.html" class="struct"
title="struct vstd::simple_pptr::PointsTo">PointsTo</a>\<V\>\>, v: V)

</div>

<div class="docblock">

Moves `v` into the location pointed to by the pointer `self`. Requires
the memory to be uninitialized, and leaves it initialized.

In the ghost perspective, this updates `perm.mem_contents()` from
`MemContents::Uninit` to `MemContents::Init(v)`.

</div>

<div id="method.take" class="section method">

<a href="../../src/vstd/simple_pptr.rs.html#467-483"
class="src rightside">Source</a>

#### pub fn <a href="#method.take" class="fn">take</a>(self, verus_tmp_perm: <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<&mut <a href="struct.PointsTo.html" class="struct"
title="struct vstd::simple_pptr::PointsTo">PointsTo</a>\<V\>\>) -\> V

</div>

<div class="docblock">

Moves `v` out of the location pointed to by the pointer `self` and
returns it. Requires the memory to be initialized, and leaves it
uninitialized.

In the ghost perspective, this updates `perm.value` from `Some(v)` to
`None`, while returning the `v` as an `exec` value.

</div>

<div id="method.replace" class="section method">

<a href="../../src/vstd/simple_pptr.rs.html#488-506"
class="src rightside">Source</a>

#### pub fn <a href="#method.replace" class="fn">replace</a>(self, verus_tmp_perm: <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<&mut <a href="struct.PointsTo.html" class="struct"
title="struct vstd::simple_pptr::PointsTo">PointsTo</a>\<V\>\>, in_v: V) -\> V

</div>

<div class="docblock">

Swaps the `in_v: V` passed in as an argument with the value in memory.
Requires the memory to be initialized, and leaves it initialized with
the new value.

</div>

<div id="method.borrow" class="section method">

<a href="../../src/vstd/simple_pptr.rs.html#510-524"
class="src rightside">Source</a>

#### pub fn <a href="#method.borrow" class="fn">borrow</a>\<'a\>(self, verus_tmp_perm: <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<&'a <a href="struct.PointsTo.html" class="struct"
title="struct vstd::simple_pptr::PointsTo">PointsTo</a>\<V\>\>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a V</a>

</div>

<div class="docblock">

Given a shared borrow of the `PointsTo<V>`, obtain a shared borrow of
`V`.

</div>

<div id="method.write" class="section method">

<a href="../../src/vstd/simple_pptr.rs.html#527-541"
class="src rightside">Source</a>

#### pub fn <a href="#method.write" class="fn">write</a>(self, verus_tmp_perm: <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<&mut <a href="struct.PointsTo.html" class="struct"
title="struct vstd::simple_pptr::PointsTo">PointsTo</a>\<V\>\>, in_v: V)

<div class="where">

where V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a>,

</div>

</div>

<div id="method.read" class="section method">

<a href="../../src/vstd/simple_pptr.rs.html#544-554"
class="src rightside">Source</a>

#### pub fn <a href="#method.read" class="fn">read</a>(self, verus_tmp_perm: <a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<&<a href="struct.PointsTo.html" class="struct"
title="struct vstd::simple_pptr::PointsTo">PointsTo</a>\<V\>\>) -\> V

<div class="where">

where V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a>,

</div>

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-PPtr%3CV%3E" class="section impl">

<a href="../../src/vstd/simple_pptr.rs.html#322-329"
class="src rightside">Source</a><a href="#impl-Clone-for-PPtr%3CV%3E" class="anchor">§</a>

### impl\<V\> <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="struct.PPtr.html" class="struct"
title="struct vstd::simple_pptr::PPtr">PPtr</a>\<V\>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../../src/vstd/simple_pptr.rs.html#323-328"
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

<div id="impl-Copy-for-PPtr%3CV%3E" class="section impl">

<a href="../../src/vstd/simple_pptr.rs.html#331-333"
class="src rightside">Source</a><a href="#impl-Copy-for-PPtr%3CV%3E" class="anchor">§</a>

### impl\<V\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a> for <a href="struct.PPtr.html" class="struct"
title="struct vstd::simple_pptr::PPtr">PPtr</a>\<V\>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-PPtr%3CV%3E" class="section impl">

<a href="#impl-Freeze-for-PPtr%3CV%3E" class="anchor">§</a>

### impl\<V\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.PPtr.html" class="struct"
title="struct vstd::simple_pptr::PPtr">PPtr</a>\<V\>

</div>

<div id="impl-RefUnwindSafe-for-PPtr%3CV%3E" class="section impl">

<a href="#impl-RefUnwindSafe-for-PPtr%3CV%3E" class="anchor">§</a>

### impl\<V\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.PPtr.html" class="struct"
title="struct vstd::simple_pptr::PPtr">PPtr</a>\<V\>

<div class="where">

where V: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,

</div>

</div>

<div id="impl-Send-for-PPtr%3CV%3E" class="section impl">

<a href="#impl-Send-for-PPtr%3CV%3E" class="anchor">§</a>

### impl\<V\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.PPtr.html" class="struct"
title="struct vstd::simple_pptr::PPtr">PPtr</a>\<V\>

<div class="where">

where V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>,

</div>

</div>

<div id="impl-Sync-for-PPtr%3CV%3E" class="section impl">

<a href="#impl-Sync-for-PPtr%3CV%3E" class="anchor">§</a>

### impl\<V\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.PPtr.html" class="struct"
title="struct vstd::simple_pptr::PPtr">PPtr</a>\<V\>

<div class="where">

where V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>,

</div>

</div>

<div id="impl-Unpin-for-PPtr%3CV%3E" class="section impl">

<a href="#impl-Unpin-for-PPtr%3CV%3E" class="anchor">§</a>

### impl\<V\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.PPtr.html" class="struct"
title="struct vstd::simple_pptr::PPtr">PPtr</a>\<V\>

<div class="where">

where V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>,

</div>

</div>

<div id="impl-UnwindSafe-for-PPtr%3CV%3E" class="section impl">

<a href="#impl-UnwindSafe-for-PPtr%3CV%3E" class="anchor">§</a>

### impl\<V\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.PPtr.html" class="struct"
title="struct vstd::simple_pptr::PPtr">PPtr</a>\<V\>

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
