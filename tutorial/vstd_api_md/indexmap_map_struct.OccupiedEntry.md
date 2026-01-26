<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[indexmap](../index.html)::[map](index.html)

</div>

# Struct <span class="struct">OccupiedEntry</span> Copy item path

<span class="sub-heading"><a href="../../src/indexmap/map/core/raw.rs.html#108-112"
class="src">Source</a> </span>

</div>

``` rust
pub struct OccupiedEntry<'a, K, V> { /* private fields */ }
```

Expand description

<div class="docblock">

A view into an occupied entry in a `IndexMap`. It is part of the
[`Entry`](enum.Entry.html) enum.

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-OccupiedEntry%3C'a,+K,+V%3E" class="section impl">

<a href="../../src/indexmap/map/core/raw.rs.html#119-191"
class="src rightside">Source</a><a href="#impl-OccupiedEntry%3C&#39;a,+K,+V%3E" class="anchor">§</a>

### impl\<'a, K, V\> <a href="struct.OccupiedEntry.html" class="struct"
title="struct indexmap::map::OccupiedEntry">OccupiedEntry</a>\<'a, K, V\>

</div>

<div class="impl-items">

<div id="method.key" class="section method">

<a href="../../src/indexmap/map/core/raw.rs.html#125-127"
class="src rightside">Source</a>

#### pub fn <a href="#method.key" class="fn">key</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>

</div>

<div class="docblock">

Gets a reference to the entry’s key in the map.

Note that this is not the key that was used to find the entry. There may
be an observable difference if the key type has any distinguishing
features outside of `Hash` and `Eq`, like extra fields or the memory
address of an allocation.

</div>

<div id="method.get" class="section method">

<a href="../../src/indexmap/map/core/raw.rs.html#130-132"
class="src rightside">Source</a>

#### pub fn <a href="#method.get" class="fn">get</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>

</div>

<div class="docblock">

Gets a reference to the entry’s value in the map.

</div>

<div id="method.get_mut" class="section method">

<a href="../../src/indexmap/map/core/raw.rs.html#138-141"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_mut" class="fn">get_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut V</a>

</div>

<div class="docblock">

Gets a mutable reference to the entry’s value in the map.

If you need a reference which may outlive the destruction of the `Entry`
value, see `into_mut`.

</div>

<div id="method.index" class="section method">

<a href="../../src/indexmap/map/core/raw.rs.html#152-155"
class="src rightside">Source</a>

#### pub fn <a href="#method.index" class="fn">index</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Return the index of the key-value pair

</div>

<div id="method.into_mut" class="section method">

<a href="../../src/indexmap/map/core/raw.rs.html#159-162"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_mut" class="fn">into_mut</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a mut V</a>

</div>

<div class="docblock">

Converts into a mutable reference to the entry’s value in the map, with
a lifetime bound to the map itself.

</div>

<div id="method.swap_remove_entry" class="section method">

<a href="../../src/indexmap/map/core/raw.rs.html#171-176"
class="src rightside">Source</a>

#### pub fn <a href="#method.swap_remove_entry" class="fn">swap_remove_entry</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(K, V)</a>

</div>

<div class="docblock">

Remove and return the key, value pair stored in the map for this entry

Like `Vec::swap_remove`, the pair is removed by swapping it with the
last element of the map and popping it off. **This perturbs the position
of what used to be the last element!**

Computes in **O(1)** time (average).

</div>

<div id="method.shift_remove_entry" class="section method">

<a href="../../src/indexmap/map/core/raw.rs.html#185-190"
class="src rightside">Source</a>

#### pub fn <a href="#method.shift_remove_entry" class="fn">shift_remove_entry</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(K, V)</a>

</div>

<div class="docblock">

Remove and return the key, value pair stored in the map for this entry

Like `Vec::remove`, the pair is removed by shifting all of the elements
that follow it, preserving their relative order. **This perturbs the
index of all of those elements!**

Computes in **O(n)** time (average).

</div>

</div>

<div id="impl-OccupiedEntry%3C'_,+K,+V%3E" class="section impl">

<a href="../../src/indexmap/map/core.rs.html#601-642"
class="src rightside">Source</a><a href="#impl-OccupiedEntry%3C&#39;_,+K,+V%3E" class="anchor">§</a>

### impl\<K, V\> <a href="struct.OccupiedEntry.html" class="struct"
title="struct indexmap::map::OccupiedEntry">OccupiedEntry</a>\<'\_, K, V\>

</div>

<div class="impl-items">

<div id="method.insert" class="section method">

<a href="../../src/indexmap/map/core.rs.html#603-605"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert" class="fn">insert</a>(&mut self, value: V) -\> V

</div>

<div class="docblock">

Sets the value of the entry to `value`, and returns the entry’s old
value.

</div>

<div id="method.remove" class="section method">

<a href="../../src/indexmap/map/core.rs.html#610-612"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove" class="fn">remove</a>(self) -\> V

</div>

<div class="docblock">

Remove the key, value pair stored in the map for this entry, and return
the value.

**NOTE:** This is equivalent to `.swap_remove()`.

</div>

<div id="method.swap_remove" class="section method">

<a href="../../src/indexmap/map/core.rs.html#621-623"
class="src rightside">Source</a>

#### pub fn <a href="#method.swap_remove" class="fn">swap_remove</a>(self) -\> V

</div>

<div class="docblock">

Remove the key, value pair stored in the map for this entry, and return
the value.

Like `Vec::swap_remove`, the pair is removed by swapping it with the
last element of the map and popping it off. **This perturbs the position
of what used to be the last element!**

Computes in **O(1)** time (average).

</div>

<div id="method.shift_remove" class="section method">

<a href="../../src/indexmap/map/core.rs.html#632-634"
class="src rightside">Source</a>

#### pub fn <a href="#method.shift_remove" class="fn">shift_remove</a>(self) -\> V

</div>

<div class="docblock">

Remove the key, value pair stored in the map for this entry, and return
the value.

Like `Vec::remove`, the pair is removed by shifting all of the elements
that follow it, preserving their relative order. **This perturbs the
index of all of those elements!**

Computes in **O(n)** time (average).

</div>

<div id="method.remove_entry" class="section method">

<a href="../../src/indexmap/map/core.rs.html#639-641"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove_entry" class="fn">remove_entry</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(K, V)</a>

</div>

<div class="docblock">

Remove and return the key, value pair stored in the map for this entry

**NOTE:** This is equivalent to `.swap_remove_entry()`.

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Debug-for-OccupiedEntry%3C'_,+K,+V%3E"
class="section impl">

<a href="../../src/indexmap/map/core.rs.html#644-651"
class="src rightside">Source</a><a href="#impl-Debug-for-OccupiedEntry%3C&#39;_,+K,+V%3E"
class="anchor">§</a>

### impl\<K: <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, V: <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.OccupiedEntry.html" class="struct"
title="struct indexmap::map::OccupiedEntry">OccupiedEntry</a>\<'\_, K, V\>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../../src/indexmap/map/core.rs.html#645-650"
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

<div id="impl-Sync-for-OccupiedEntry%3C'_,+K,+V%3E"
class="section impl">

<a href="../../src/indexmap/map/core/raw.rs.html#116"
class="src rightside">Source</a><a href="#impl-Sync-for-OccupiedEntry%3C&#39;_,+K,+V%3E"
class="anchor">§</a>

### impl\<K: <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, V: <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.OccupiedEntry.html" class="struct"
title="struct indexmap::map::OccupiedEntry">OccupiedEntry</a>\<'\_, K, V\>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-OccupiedEntry%3C'a,+K,+V%3E"
class="section impl">

<a href="#impl-Freeze-for-OccupiedEntry%3C&#39;a,+K,+V%3E"
class="anchor">§</a>

### impl\<'a, K, V\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.OccupiedEntry.html" class="struct"
title="struct indexmap::map::OccupiedEntry">OccupiedEntry</a>\<'a, K, V\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a>,

</div>

</div>

<div id="impl-RefUnwindSafe-for-OccupiedEntry%3C'a,+K,+V%3E"
class="section impl">

<a href="#impl-RefUnwindSafe-for-OccupiedEntry%3C&#39;a,+K,+V%3E"
class="anchor">§</a>

### impl\<'a, K, V\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.OccupiedEntry.html" class="struct"
title="struct indexmap::map::OccupiedEntry">OccupiedEntry</a>\<'a, K, V\>

<div class="where">

where K: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
V: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,

</div>

</div>

<div id="impl-Send-for-OccupiedEntry%3C'a,+K,+V%3E"
class="section impl">

<a href="#impl-Send-for-OccupiedEntry%3C&#39;a,+K,+V%3E"
class="anchor">§</a>

### impl\<'a, K, V\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.OccupiedEntry.html" class="struct"
title="struct indexmap::map::OccupiedEntry">OccupiedEntry</a>\<'a, K, V\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>,

</div>

</div>

<div id="impl-Unpin-for-OccupiedEntry%3C'a,+K,+V%3E"
class="section impl">

<a href="#impl-Unpin-for-OccupiedEntry%3C&#39;a,+K,+V%3E"
class="anchor">§</a>

### impl\<'a, K, V\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.OccupiedEntry.html" class="struct"
title="struct indexmap::map::OccupiedEntry">OccupiedEntry</a>\<'a, K, V\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>,

</div>

</div>

<div id="impl-UnwindSafe-for-OccupiedEntry%3C'a,+K,+V%3E"
class="section impl">

<a href="#impl-UnwindSafe-for-OccupiedEntry%3C&#39;a,+K,+V%3E"
class="anchor">§</a>

### impl\<'a, K, V\> \!<a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.OccupiedEntry.html" class="struct"
title="struct indexmap::map::OccupiedEntry">OccupiedEntry</a>\<'a, K, V\>

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
