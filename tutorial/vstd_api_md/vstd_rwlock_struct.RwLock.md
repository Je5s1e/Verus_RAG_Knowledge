<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[rwlock](index.html)

</div>

# Struct <span class="struct">RwLock</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/rwlock.rs.html#337-344" class="src">Source</a>
</span>

</div>

``` rust
pub struct RwLock<V, Pred: RwLockPredicate<V>> { /* private fields */ }
```

Expand description

<div class="docblock">

A verified implementation of a reader-writer lock, implemented using
atomics and a reference count.

When constructed, you can provide an invariant via the `Pred` parameter,
specifying the allowed values that can go in the lock.

Note that this specification does *not* verify the absence of
dead-locks.

#### <a href="#examples" class="doc-anchor">§</a>Examples

On construction of a lock, we can specify an invariant for the object
that goes inside. One way to do this is by providing a `spec_fn`, which
implements the
[`RwLockPredicate`](trait.RwLockPredicate.html "trait vstd::rwlock::RwLockPredicate")
trait.

<div class="example-wrap ignore">

<a href="#" class="tooltip" title="This example is not tested">ⓘ</a>

``` rust
fn example1() {
    // We can create a lock with an invariant: `v == 5 || v == 13`.
    // Thus only 5 or 13 can be stored in the lock.
    let lock = RwLock::<u64, spec_fn(u64) -> bool>::new(5, Ghost(|v| v == 5 || v == 13));

    let (val, write_handle) = lock.acquire_write();
    assert(val == 5 || val == 13);
    write_handle.release_write(13);

    let read_handle1 = lock.acquire_read();
    let read_handle2 = lock.acquire_read();

    // We can take multiple read handles at the same time:

    let val1 = read_handle1.borrow();
    let val2 = read_handle2.borrow();

    // RwLock has a lemma that both read handles have the same value:

    proof { ReadHandle::lemma_readers_match(&read_handle1, &read_handle2); }
    assert(*val1 == *val2);

    read_handle1.release_read();
    read_handle2.release_read();
}
```

</div>

It’s often easier to implement the
[`RwLockPredicate`](trait.RwLockPredicate.html "trait vstd::rwlock::RwLockPredicate")
trait yourself. This way you can have a configurable predicate without
needing to work with higher-order functions.

<div class="example-wrap ignore">

<a href="#" class="tooltip" title="This example is not tested">ⓘ</a>

``` rust
struct FixedParity {
    pub parity: int,
}

impl RwLockPredicate<u64> for FixedParity {
    open spec fn inv(self, v: u64) -> bool {
        v % 2 == self.parity
    }
}

fn example2() {
    // Create a lock that can only store even integers
    let lock_even = RwLock::<u64, FixedParity>::new(20, Ghost(FixedParity { parity: 0 }));

    // Create a lock that can only store odd integers
    let lock_odd = RwLock::<u64, FixedParity>::new(23, Ghost(FixedParity { parity: 1 }));

    let read_handle_even = lock_even.acquire_read();
    let val_even = *read_handle_even.borrow();
    assert(val_even % 2 == 0);

    let read_handle_odd = lock_odd.acquire_read();
    let val_odd = *read_handle_odd.borrow();
    assert(val_odd % 2 == 1);
}
```

</div>

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-RwLock%3CV,+Pred%3E" class="section impl">

<a href="../../src/vstd/rwlock.rs.html#489-704"
class="src rightside">Source</a><a href="#impl-RwLock%3CV,+Pred%3E" class="anchor">§</a>

### impl\<V, Pred: <a href="trait.RwLockPredicate.html" class="trait"
title="trait vstd::rwlock::RwLockPredicate">RwLockPredicate</a>\<V\>\> <a href="struct.RwLock.html" class="struct"
title="struct vstd::rwlock::RwLock">RwLock</a>\<V, Pred\>

</div>

<div class="impl-items">

<div id="method.new" class="section method">

<a href="../../src/vstd/rwlock.rs.html#501-521"
class="src rightside">Source</a>

#### pub fn <a href="#method.new" class="fn">new</a>(val: V, verus_tmp_pred: <a href="../prelude/struct.Ghost.html" class="struct"
title="struct vstd::prelude::Ghost">Ghost</a>\<Pred\>) -\> Self

</div>

<div id="method.acquire_write" class="section method">

<a href="../../src/vstd/rwlock.rs.html#529-611"
class="src rightside">Source</a>

#### pub fn <a href="#method.acquire_write" class="fn">acquire_write</a>(&self) -\> (V, <a href="struct.WriteHandle.html" class="struct"
title="struct vstd::rwlock::WriteHandle">WriteHandle</a>\<'\_, V, Pred\>)

</div>

<div class="docblock">

Acquires an exclusive write-lock. To release it, use
[`WriteHandle::release_write`](struct.WriteHandle.html#method.release_write "method vstd::rwlock::WriteHandle::release_write").

**Warning:** The lock is *NOT* released automatically when the handle is
dropped. You must call
[`WriteHandle::release_write`](struct.WriteHandle.html#method.release_write "method vstd::rwlock::WriteHandle::release_write").
Verus does not check that lock is released.

</div>

<div id="method.acquire_read" class="section method">

<a href="../../src/vstd/rwlock.rs.html#619-692"
class="src rightside">Source</a>

#### pub fn <a href="#method.acquire_read" class="fn">acquire_read</a>(&self) -\> <a href="struct.ReadHandle.html" class="struct"
title="struct vstd::rwlock::ReadHandle">ReadHandle</a>\<'\_, V, Pred\>

</div>

<div class="docblock">

Acquires a shared read-lock. To release it, use
[`ReadHandle::release_read`](struct.ReadHandle.html#method.release_read "method vstd::rwlock::ReadHandle::release_read").

**Warning:** The lock is *NOT* released automatically when the handle is
dropped. You must call
[`ReadHandle::release_read`](struct.ReadHandle.html#method.release_read "method vstd::rwlock::ReadHandle::release_read").
Verus does not check that lock is released.

</div>

<div id="method.into_inner" class="section method">

<a href="../../src/vstd/rwlock.rs.html#697-703"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_inner" class="fn">into_inner</a>(self) -\> V

</div>

<div class="docblock">

Destroys the lock and returns the inner object. Note that this may
deadlock if not all locks have been released.

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-RwLock%3CV,+Pred%3E" class="section impl">

<a href="#impl-Freeze-for-RwLock%3CV,+Pred%3E" class="anchor">§</a>

### impl\<V, Pred\> \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.RwLock.html" class="struct"
title="struct vstd::rwlock::RwLock">RwLock</a>\<V, Pred\>

</div>

<div id="impl-RefUnwindSafe-for-RwLock%3CV,+Pred%3E"
class="section impl">

<a href="#impl-RefUnwindSafe-for-RwLock%3CV,+Pred%3E"
class="anchor">§</a>

### impl\<V, Pred\> \!<a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.RwLock.html" class="struct"
title="struct vstd::rwlock::RwLock">RwLock</a>\<V, Pred\>

</div>

<div id="impl-Send-for-RwLock%3CV,+Pred%3E" class="section impl">

<a href="#impl-Send-for-RwLock%3CV,+Pred%3E" class="anchor">§</a>

### impl\<V, Pred\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.RwLock.html" class="struct"
title="struct vstd::rwlock::RwLock">RwLock</a>\<V, Pred\>

<div class="where">

where Pred:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>,

</div>

</div>

<div id="impl-Sync-for-RwLock%3CV,+Pred%3E" class="section impl">

<a href="#impl-Sync-for-RwLock%3CV,+Pred%3E" class="anchor">§</a>

### impl\<V, Pred\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.RwLock.html" class="struct"
title="struct vstd::rwlock::RwLock">RwLock</a>\<V, Pred\>

<div class="where">

where Pred:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>,

</div>

</div>

<div id="impl-Unpin-for-RwLock%3CV,+Pred%3E" class="section impl">

<a href="#impl-Unpin-for-RwLock%3CV,+Pred%3E" class="anchor">§</a>

### impl\<V, Pred\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.RwLock.html" class="struct"
title="struct vstd::rwlock::RwLock">RwLock</a>\<V, Pred\>

<div class="where">

where Pred:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>,

</div>

</div>

<div id="impl-UnwindSafe-for-RwLock%3CV,+Pred%3E" class="section impl">

<a href="#impl-UnwindSafe-for-RwLock%3CV,+Pred%3E" class="anchor">§</a>

### impl\<V, Pred\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.RwLock.html" class="struct"
title="struct vstd::rwlock::RwLock">RwLock</a>\<V, Pred\>

<div class="where">

where Pred: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
V: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,

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
