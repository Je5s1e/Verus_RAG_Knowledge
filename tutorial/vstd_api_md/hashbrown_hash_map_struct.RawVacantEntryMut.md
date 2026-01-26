<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[hashbrown](../index.html)::[hash_map](index.html)

</div>

# Struct <span class="struct">RawVacantEntryMut</span> Copy item path

<span class="sub-heading"><a href="../../src/hashbrown/map.rs.html#3044-3047"
class="src">Source</a> </span>

</div>

``` rust
pub struct RawVacantEntryMut<'a, K, V, S, A: Allocator + Clone = Global> { /* private fields */ }
```

Expand description

<div class="docblock">

A view into a vacant entry in a `HashMap`. It is part of the
[`RawEntryMut`](enum.RawEntryMut.html) enum.

## <a href="#examples" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use core::hash::{BuildHasher, Hash};
use hashbrown::hash_map::{HashMap, RawEntryMut, RawVacantEntryMut};

let mut map = HashMap::<&str, i32>::new();

fn compute_hash<K: Hash + ?Sized, S: BuildHasher>(hash_builder: &S, key: &K) -> u64 {
    use core::hash::Hasher;
    let mut state = hash_builder.build_hasher();
    key.hash(&mut state);
    state.finish()
}

let raw_v: RawVacantEntryMut<_, _, _> = match map.raw_entry_mut().from_key(&"a") {
    RawEntryMut::Vacant(view) => view,
    RawEntryMut::Occupied(_) => unreachable!(),
};
raw_v.insert("a", 10);
assert!(map[&"a"] == 10 && map.len() == 1);

// Nonexistent key (insert and update)
let hash = compute_hash(map.hasher(), &"b");
match map.raw_entry_mut().from_key_hashed_nocheck(hash, &"b") {
    RawEntryMut::Occupied(_) => unreachable!(),
    RawEntryMut::Vacant(view) => {
        let (k, value) = view.insert("b", 2);
        assert_eq!((*k, *value), ("b", 2));
        *value = 20;
    }
}
assert!(map[&"b"] == 20 && map.len() == 2);

let hash = compute_hash(map.hasher(), &"c");
match map.raw_entry_mut().from_hash(hash, |q| *q == "c") {
    RawEntryMut::Occupied(_) => unreachable!(),
    RawEntryMut::Vacant(view) => {
        assert_eq!(view.insert("c", 30), (&mut "c", &mut 30));
    }
}
assert!(map[&"c"] == 30 && map.len() == 3);
```

</div>

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-RawVacantEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#3885-4029"
class="src rightside">Source</a><a href="#impl-RawVacantEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="struct.RawVacantEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawVacantEntryMut">RawVacantEntryMut</a>\<'a, K, V, S, A\>

</div>

<div class="impl-items">

<div id="method.insert" class="section method">

<a href="../../src/hashbrown/map.rs.html#3904-3911"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert" class="fn">insert</a>(self, key: K, value: V) -\> (<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut K</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut V</a>)

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

##### <a href="#examples-1" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{HashMap, RawEntryMut};

let mut map: HashMap<&str, u32> = [("a", 100), ("b", 200)].into();

match map.raw_entry_mut().from_key(&"c") {
    RawEntryMut::Occupied(_) => panic!(),
    RawEntryMut::Vacant(v) => assert_eq!(v.insert("c", 300), (&mut "c", &mut 300)),
}

assert_eq!(map[&"c"], 300);
```

</div>

</div>

<div id="method.insert_hashed_nocheck" class="section method">

<a href="../../src/hashbrown/map.rs.html#3945-3956"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert_hashed_nocheck"
class="fn">insert_hashed_nocheck</a>( self, hash: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>, key: K, value: V, ) -\> (<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut K</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut V</a>)

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

##### <a href="#examples-2" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use core::hash::{BuildHasher, Hash};
use hashbrown::hash_map::{HashMap, RawEntryMut};

fn compute_hash<K: Hash + ?Sized, S: BuildHasher>(hash_builder: &S, key: &K) -> u64 {
    use core::hash::Hasher;
    let mut state = hash_builder.build_hasher();
    key.hash(&mut state);
    state.finish()
}

let mut map: HashMap<&str, u32> = [("a", 100), ("b", 200)].into();
let key = "c";
let hash = compute_hash(map.hasher(), &key);

match map.raw_entry_mut().from_key_hashed_nocheck(hash, &key) {
    RawEntryMut::Occupied(_) => panic!(),
    RawEntryMut::Vacant(v) => assert_eq!(
        v.insert_hashed_nocheck(hash, key, 300),
        (&mut "c", &mut 300)
    ),
}

assert_eq!(map[&"c"], 300);
```

</div>

</div>

<div id="method.insert_with_hasher" class="section method">

<a href="../../src/hashbrown/map.rs.html#3995-4009"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert_with_hasher" class="fn">insert_with_hasher</a>\<H\>( self, hash: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>, key: K, value: V, hasher: H, ) -\> (<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut K</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut V</a>)

<div class="where">

where H: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.Fn.html"
class="trait" title="trait core::ops::function::Fn">Fn</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;K</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>,

</div>

</div>

<div class="docblock">

Set the value of an entry with a custom hasher function.

##### <a href="#examples-3" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use core::hash::{BuildHasher, Hash};
use hashbrown::hash_map::{HashMap, RawEntryMut};

fn make_hasher<K, S>(hash_builder: &S) -> impl Fn(&K) -> u64 + '_
where
    K: Hash + ?Sized,
    S: BuildHasher,
{
    move |key: &K| {
        use core::hash::Hasher;
        let mut state = hash_builder.build_hasher();
        key.hash(&mut state);
        state.finish()
    }
}

let mut map: HashMap<&str, u32> = HashMap::new();
let key = "a";
let hash_builder = map.hasher().clone();
let hash = make_hasher(&hash_builder)(&key);

match map.raw_entry_mut().from_hash(hash, |q| q == &key) {
    RawEntryMut::Occupied(_) => panic!(),
    RawEntryMut::Vacant(v) => assert_eq!(
        v.insert_with_hasher(hash, key, 100, make_hasher(&hash_builder)),
        (&mut "a", &mut 100)
    ),
}
map.extend([("b", 200), ("c", 300), ("d", 400), ("e", 500), ("f", 600)]);
assert_eq!(map[&"a"], 100);
```

</div>

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Debug-for-RawVacantEntryMut%3C'_,+K,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#4055-4059"
class="src rightside">Source</a><a href="#impl-Debug-for-RawVacantEntryMut%3C&#39;_,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<K, V, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.RawVacantEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawVacantEntryMut">RawVacantEntryMut</a>\<'\_, K, V, S, A\>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#4056-4058"
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

<div id="impl-Freeze-for-RawVacantEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Freeze-for-RawVacantEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.RawVacantEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawVacantEntryMut">RawVacantEntryMut</a>\<'a, K, V, S, A\>

</div>

<div id="impl-RefUnwindSafe-for-RawVacantEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a
href="#impl-RefUnwindSafe-for-RawVacantEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.RawVacantEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawVacantEntryMut">RawVacantEntryMut</a>\<'a, K, V, S, A\>

<div class="where">

where S: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
A: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
K: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
V: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,

</div>

</div>

<div id="impl-Send-for-RawVacantEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Send-for-RawVacantEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.RawVacantEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawVacantEntryMut">RawVacantEntryMut</a>\<'a, K, V, S, A\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>,

</div>

</div>

<div id="impl-Sync-for-RawVacantEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Sync-for-RawVacantEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.RawVacantEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawVacantEntryMut">RawVacantEntryMut</a>\<'a, K, V, S, A\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>,

</div>

</div>

<div id="impl-Unpin-for-RawVacantEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Unpin-for-RawVacantEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.RawVacantEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawVacantEntryMut">RawVacantEntryMut</a>\<'a, K, V, S, A\>

</div>

<div id="impl-UnwindSafe-for-RawVacantEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-UnwindSafe-for-RawVacantEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A = Global\> \!<a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.RawVacantEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawVacantEntryMut">RawVacantEntryMut</a>\<'a, K, V, S, A\>

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
