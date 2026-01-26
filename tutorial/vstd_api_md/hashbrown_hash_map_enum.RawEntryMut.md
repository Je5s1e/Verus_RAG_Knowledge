<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[hashbrown](../index.html)::[hash_map](index.html)

</div>

# Enum <span class="enum">RawEntryMut</span> Copy item path

<span class="sub-heading"><a href="../../src/hashbrown/map.rs.html#2882-2911"
class="src">Source</a> </span>

</div>

``` rust
pub enum RawEntryMut<'a, K, V, S, A: Allocator + Clone = Global> {
    Occupied(RawOccupiedEntryMut<'a, K, V, S, A>),
    Vacant(RawVacantEntryMut<'a, K, V, S, A>),
}
```

Expand description

<div class="docblock">

A view into a single entry in a map, which may either be vacant or
occupied.

This is a lower-level version of [`Entry`](enum.Entry.html).

This `enum` is constructed through the
[`raw_entry_mut`](struct.HashMap.html#method.raw_entry_mut) method on
[`HashMap`](struct.HashMap.html), then calling one of the methods of
that [`RawEntryBuilderMut`](struct.RawEntryBuilderMut.html).

## <a href="#examples" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use core::hash::{BuildHasher, Hash};
use hashbrown::hash_map::{HashMap, RawEntryMut, RawOccupiedEntryMut};

let mut map = HashMap::new();
map.extend([('a', 1), ('b', 2), ('c', 3)]);
assert_eq!(map.len(), 3);

fn compute_hash<K: Hash + ?Sized, S: BuildHasher>(hash_builder: &S, key: &K) -> u64 {
    use core::hash::Hasher;
    let mut state = hash_builder.build_hasher();
    key.hash(&mut state);
    state.finish()
}

// Existing key (insert)
let raw: RawEntryMut<_, _, _> = map.raw_entry_mut().from_key(&'a');
let _raw_o: RawOccupiedEntryMut<_, _, _> = raw.insert('a', 10);
assert_eq!(map.len(), 3);

// Nonexistent key (insert)
map.raw_entry_mut().from_key(&'d').insert('d', 40);
assert_eq!(map.len(), 4);

// Existing key (or_insert)
let hash = compute_hash(map.hasher(), &'b');
let kv = map
    .raw_entry_mut()
    .from_key_hashed_nocheck(hash, &'b')
    .or_insert('b', 20);
assert_eq!(kv, (&mut 'b', &mut 2));
*kv.1 = 20;
assert_eq!(map.len(), 4);

// Nonexistent key (or_insert)
let hash = compute_hash(map.hasher(), &'e');
let kv = map
    .raw_entry_mut()
    .from_key_hashed_nocheck(hash, &'e')
    .or_insert('e', 50);
assert_eq!(kv, (&mut 'e', &mut 50));
assert_eq!(map.len(), 5);

// Existing key (or_insert_with)
let hash = compute_hash(map.hasher(), &'c');
let kv = map
    .raw_entry_mut()
    .from_hash(hash, |q| q == &'c')
    .or_insert_with(|| ('c', 30));
assert_eq!(kv, (&mut 'c', &mut 3));
*kv.1 = 30;
assert_eq!(map.len(), 5);

// Nonexistent key (or_insert_with)
let hash = compute_hash(map.hasher(), &'f');
let kv = map
    .raw_entry_mut()
    .from_hash(hash, |q| q == &'f')
    .or_insert_with(|| ('f', 60));
assert_eq!(kv, (&mut 'f', &mut 60));
assert_eq!(map.len(), 6);

println!("Our HashMap: {:?}", map);

let mut vec: Vec<_> = map.iter().map(|(&k, &v)| (k, v)).collect();
// The `Iter` iterator produces items in arbitrary order, so the
// items must be sorted to test them against a sorted array.
vec.sort_unstable();
assert_eq!(vec, [('a', 10), ('b', 20), ('c', 30), ('d', 40), ('e', 50), ('f', 60)]);
```

</div>

</div>

## Variants<a href="#variants" class="anchor">§</a>

<div class="variants">

<div id="variant.Occupied" class="section variant">

<a href="#variant.Occupied" class="anchor">§</a>

### Occupied(<a href="struct.RawOccupiedEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawOccupiedEntryMut">RawOccupiedEntryMut</a>\<'a, K, V, S, A\>)

</div>

<div class="docblock">

An occupied entry.

#### <a href="#examples-1" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::{hash_map::RawEntryMut, HashMap};
let mut map: HashMap<_, _> = [("a", 100), ("b", 200)].into();

match map.raw_entry_mut().from_key(&"a") {
    RawEntryMut::Vacant(_) => unreachable!(),
    RawEntryMut::Occupied(_) => { }
}
```

</div>

</div>

<div id="variant.Vacant" class="section variant">

<a href="#variant.Vacant" class="anchor">§</a>

### Vacant(<a href="struct.RawVacantEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawVacantEntryMut">RawVacantEntryMut</a>\<'a, K, V, S, A\>)

</div>

<div class="docblock">

A vacant entry.

#### <a href="#examples-2" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::{hash_map::RawEntryMut, HashMap};
let mut map: HashMap<&str, i32> = HashMap::new();

match map.raw_entry_mut().from_key("a") {
    RawEntryMut::Occupied(_) => unreachable!(),
    RawEntryMut::Vacant(_) => { }
}
```

</div>

</div>

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-RawEntryMut%3C'a,+K,+V,+S,+A%3E" class="section impl">

<a href="../../src/hashbrown/map.rs.html#3292-3484"
class="src rightside">Source</a><a href="#impl-RawEntryMut%3C&#39;a,+K,+V,+S,+A%3E" class="anchor">§</a>

### impl\<'a, K, V, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="enum.RawEntryMut.html" class="enum"
title="enum hashbrown::hash_map::RawEntryMut">RawEntryMut</a>\<'a, K, V, S, A\>

</div>

<div class="impl-items">

<div id="method.insert" class="section method">

<a href="../../src/hashbrown/map.rs.html#3306-3318"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert" class="fn">insert</a>(self, key: K, value: V) -\> <a href="struct.RawOccupiedEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawOccupiedEntryMut">RawOccupiedEntryMut</a>\<'a, K, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="docblock">

Sets the value of the entry, and returns a RawOccupiedEntryMut.

##### <a href="#examples-3" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<&str, u32> = HashMap::new();
let entry = map.raw_entry_mut().from_key("horseyland").insert("horseyland", 37);

assert_eq!(entry.remove_entry(), ("horseyland", 37));
```

</div>

</div>

<div id="method.or_insert" class="section method">

<a href="../../src/hashbrown/map.rs.html#3337-3346"
class="src rightside">Source</a>

#### pub fn <a href="#method.or_insert" class="fn">or_insert</a>(self, default_key: K, default_val: V) -\> (<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
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

Ensures a value is in the entry by inserting the default if empty, and
returns mutable references to the key and value in the entry.

##### <a href="#examples-4" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<&str, u32> = HashMap::new();

map.raw_entry_mut().from_key("poneyland").or_insert("poneyland", 3);
assert_eq!(map["poneyland"], 3);

*map.raw_entry_mut().from_key("poneyland").or_insert("poneyland", 10).1 *= 2;
assert_eq!(map["poneyland"], 6);
```

</div>

</div>

<div id="method.or_insert_with" class="section method">

<a href="../../src/hashbrown/map.rs.html#3365-3378"
class="src rightside">Source</a>

#### pub fn <a href="#method.or_insert_with" class="fn">or_insert_with</a>\<F\>(self, default: F) -\> (<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut K</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut V</a>)

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnOnce.html"
class="trait" title="trait core::ops::function::FnOnce">FnOnce</a>() -\>
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(K, V)</a>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="docblock">

Ensures a value is in the entry by inserting the result of the default
function if empty, and returns mutable references to the key and value
in the entry.

##### <a href="#examples-5" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<&str, String> = HashMap::new();

map.raw_entry_mut().from_key("poneyland").or_insert_with(|| {
    ("poneyland", "hoho".to_string())
});

assert_eq!(map["poneyland"], "hoho".to_string());
```

</div>

</div>

<div id="method.and_modify" class="section method">

<a href="../../src/hashbrown/map.rs.html#3403-3417"
class="src rightside">Source</a>

#### pub fn <a href="#method.and_modify" class="fn">and_modify</a>\<F\>(self, f: F) -\> Self

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnOnce.html"
class="trait" title="trait core::ops::function::FnOnce">FnOnce</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut K</a>,
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut V</a>),

</div>

</div>

<div class="docblock">

Provides in-place mutable access to an occupied entry before any
potential inserts into the map.

##### <a href="#examples-6" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<&str, u32> = HashMap::new();

map.raw_entry_mut()
   .from_key("poneyland")
   .and_modify(|_k, v| { *v += 1 })
   .or_insert("poneyland", 42);
assert_eq!(map["poneyland"], 42);

map.raw_entry_mut()
   .from_key("poneyland")
   .and_modify(|_k, v| { *v += 1 })
   .or_insert("poneyland", 0);
assert_eq!(map["poneyland"], 43);
```

</div>

</div>

<div id="method.and_replace_entry_with" class="section method">

<a href="../../src/hashbrown/map.rs.html#3475-3483"
class="src rightside">Source</a>

#### pub fn <a href="#method.and_replace_entry_with"
class="fn">and_replace_entry_with</a>\<F\>(self, f: F) -\> Self

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnOnce.html"
class="trait" title="trait core::ops::function::FnOnce">FnOnce</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;K</a>, V) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<V\>,

</div>

</div>

<div class="docblock">

Provides shared access to the key and owned access to the value of an
occupied entry and allows to replace or remove it based on the value of
the returned option.

##### <a href="#examples-7" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use hashbrown::hash_map::RawEntryMut;

let mut map: HashMap<&str, u32> = HashMap::new();

let entry = map
    .raw_entry_mut()
    .from_key("poneyland")
    .and_replace_entry_with(|_k, _v| panic!());

match entry {
    RawEntryMut::Vacant(_) => {},
    RawEntryMut::Occupied(_) => panic!(),
}

map.insert("poneyland", 42);

let entry = map
    .raw_entry_mut()
    .from_key("poneyland")
    .and_replace_entry_with(|k, v| {
        assert_eq!(k, &"poneyland");
        assert_eq!(v, 42);
        Some(v + 1)
    });

match entry {
    RawEntryMut::Occupied(e) => {
        assert_eq!(e.key(), &"poneyland");
        assert_eq!(e.get(), &43);
    },
    RawEntryMut::Vacant(_) => panic!(),
}

assert_eq!(map["poneyland"], 43);

let entry = map
    .raw_entry_mut()
    .from_key("poneyland")
    .and_replace_entry_with(|_k, _v| None);

match entry {
    RawEntryMut::Vacant(_) => {},
    RawEntryMut::Occupied(_) => panic!(),
}

assert!(!map.contains_key("poneyland"));
```

</div>

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Debug-for-RawEntryMut%3C'_,+K,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#4037-4044"
class="src rightside">Source</a><a href="#impl-Debug-for-RawEntryMut%3C&#39;_,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<K: <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, V: <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="enum.RawEntryMut.html" class="enum"
title="enum hashbrown::hash_map::RawEntryMut">RawEntryMut</a>\<'\_, K, V, S, A\>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#4038-4043"
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

<div id="impl-Freeze-for-RawEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Freeze-for-RawEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="enum.RawEntryMut.html" class="enum"
title="enum hashbrown::hash_map::RawEntryMut">RawEntryMut</a>\<'a, K, V, S, A\>

</div>

<div id="impl-RefUnwindSafe-for-RawEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-RefUnwindSafe-for-RawEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="enum.RawEntryMut.html" class="enum"
title="enum hashbrown::hash_map::RawEntryMut">RawEntryMut</a>\<'a, K, V, S, A\>

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

<div id="impl-Send-for-RawEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Send-for-RawEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="enum.RawEntryMut.html" class="enum"
title="enum hashbrown::hash_map::RawEntryMut">RawEntryMut</a>\<'a, K, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>,

</div>

</div>

<div id="impl-Sync-for-RawEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Sync-for-RawEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="enum.RawEntryMut.html" class="enum"
title="enum hashbrown::hash_map::RawEntryMut">RawEntryMut</a>\<'a, K, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>,

</div>

</div>

<div id="impl-Unpin-for-RawEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Unpin-for-RawEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="enum.RawEntryMut.html" class="enum"
title="enum hashbrown::hash_map::RawEntryMut">RawEntryMut</a>\<'a, K, V, S, A\>

</div>

<div id="impl-UnwindSafe-for-RawEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-UnwindSafe-for-RawEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A = Global\> \!<a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="enum.RawEntryMut.html" class="enum"
title="enum hashbrown::hash_map::RawEntryMut">RawEntryMut</a>\<'a, K, V, S, A\>

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
