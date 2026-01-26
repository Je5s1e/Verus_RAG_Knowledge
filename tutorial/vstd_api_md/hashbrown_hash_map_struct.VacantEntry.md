<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[hashbrown](../index.html)::[hash_map](index.html)

</div>

# Struct <span class="struct">VacantEntry</span> Copy item path

<span class="sub-heading"><a href="../../src/hashbrown/map.rs.html#4257-4261"
class="src">Source</a> </span>

</div>

``` rust
pub struct VacantEntry<'a, K, V, S, A: Allocator + Clone = Global> { /* private fields */ }
```

Expand description

<div class="docblock">

A view into a vacant entry in a `HashMap`. It is part of the
[`Entry`](enum.Entry.html) enum.

## <a href="#examples" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{Entry, HashMap, VacantEntry};

let mut map = HashMap::<&str, i32>::new();

let entry_v: VacantEntry<_, _, _> = match map.entry("a") {
    Entry::Vacant(view) => view,
    Entry::Occupied(_) => unreachable!(),
};
entry_v.insert(10);
assert!(map[&"a"] == 10 && map.len() == 1);

// Nonexistent key (insert and update)
match map.entry("b") {
    Entry::Occupied(_) => unreachable!(),
    Entry::Vacant(view) => {
        let value = view.insert(2);
        assert_eq!(*value, 2);
        *value = 20;
    }
}
assert!(map[&"b"] == 20 && map.len() == 2);
```

</div>

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-VacantEntry%3C'a,+K,+V,+S,+A%3E" class="section impl">

<a href="../../src/hashbrown/map.rs.html#5508-5593"
class="src rightside">Source</a><a href="#impl-VacantEntry%3C&#39;a,+K,+V,+S,+A%3E" class="anchor">§</a>

### impl\<'a, K, V, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="struct.VacantEntry.html" class="struct"
title="struct hashbrown::hash_map::VacantEntry">VacantEntry</a>\<'a, K, V, S, A\>

</div>

<div class="impl-items">

<div id="method.key" class="section method">

<a href="../../src/hashbrown/map.rs.html#5521-5523"
class="src rightside">Source</a>

#### pub fn <a href="#method.key" class="fn">key</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;K</a>

</div>

<div class="docblock">

Gets a reference to the key that would be used when inserting a value
through the `VacantEntry`.

##### <a href="#examples-1" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<&str, u32> = HashMap::new();
assert_eq!(map.entry("poneyland").key(), &"poneyland");
```

</div>

</div>

<div id="method.into_key" class="section method">

<a href="../../src/hashbrown/map.rs.html#5540-5542"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_key" class="fn">into_key</a>(self) -\> K

</div>

<div class="docblock">

Take ownership of the key.

##### <a href="#examples-2" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{Entry, HashMap};

let mut map: HashMap<&str, u32> = HashMap::new();

match map.entry("poneyland") {
    Entry::Occupied(_) => panic!(),
    Entry::Vacant(v) => assert_eq!(v.into_key(), "poneyland"),
}
```

</div>

</div>

<div id="method.insert" class="section method">

<a href="../../src/hashbrown/map.rs.html#5561-5573"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert" class="fn">insert</a>(self, value: V) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut V</a>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="docblock">

Sets the value of the entry with the VacantEntry’s key, and returns a
mutable reference to it.

##### <a href="#examples-3" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use hashbrown::hash_map::Entry;

let mut map: HashMap<&str, u32> = HashMap::new();

if let Entry::Vacant(o) = map.entry("poneyland") {
    o.insert(37);
}
assert_eq!(map["poneyland"], 37);
```

</div>

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Debug-for-VacantEntry%3C'_,+K,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#4263-4267"
class="src rightside">Source</a><a href="#impl-Debug-for-VacantEntry%3C&#39;_,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<K: <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, V, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.VacantEntry.html" class="struct"
title="struct hashbrown::hash_map::VacantEntry">VacantEntry</a>\<'\_, K, V, S, A\>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#4264-4266"
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

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-VacantEntry%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Freeze-for-VacantEntry%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.VacantEntry.html" class="struct"
title="struct hashbrown::hash_map::VacantEntry">VacantEntry</a>\<'a, K, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a>,

</div>

</div>

<div id="impl-RefUnwindSafe-for-VacantEntry%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-RefUnwindSafe-for-VacantEntry%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.VacantEntry.html" class="struct"
title="struct hashbrown::hash_map::VacantEntry">VacantEntry</a>\<'a, K, V, S, A\>

<div class="where">

where K: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
S: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
A: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
V: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,

</div>

</div>

<div id="impl-Send-for-VacantEntry%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Send-for-VacantEntry%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.VacantEntry.html" class="struct"
title="struct hashbrown::hash_map::VacantEntry">VacantEntry</a>\<'a, K, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>,

</div>

</div>

<div id="impl-Sync-for-VacantEntry%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Sync-for-VacantEntry%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.VacantEntry.html" class="struct"
title="struct hashbrown::hash_map::VacantEntry">VacantEntry</a>\<'a, K, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>,

</div>

</div>

<div id="impl-Unpin-for-VacantEntry%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Unpin-for-VacantEntry%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.VacantEntry.html" class="struct"
title="struct hashbrown::hash_map::VacantEntry">VacantEntry</a>\<'a, K, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>,

</div>

</div>

<div id="impl-UnwindSafe-for-VacantEntry%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-UnwindSafe-for-VacantEntry%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A = Global\> \!<a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.VacantEntry.html" class="struct"
title="struct hashbrown::hash_map::VacantEntry">VacantEntry</a>\<'a, K, V, S, A\>

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
class="fn">borrow</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
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
class="fn">borrow_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
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
