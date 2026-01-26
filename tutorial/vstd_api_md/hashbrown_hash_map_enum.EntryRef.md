<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[hashbrown](../index.html)::[hash_map](index.html)

</div>

# Enum <span class="enum">EntryRef</span> Copy item path

<span class="sub-heading"><a href="../../src/hashbrown/map.rs.html#4321-4354"
class="src">Source</a> </span>

</div>

``` rust
pub enum EntryRef<'a, 'b, K, Q: ?Sized, V, S, A = Global>where
    A: Allocator + Clone,{
    Occupied(OccupiedEntryRef<'a, 'b, K, Q, V, S, A>),
    Vacant(VacantEntryRef<'a, 'b, K, Q, V, S, A>),
}
```

Expand description

<div class="docblock">

A view into a single entry in a map, which may either be vacant or
occupied, with any borrowed form of the map’s key type.

This `enum` is constructed from the
[`entry_ref`](struct.HashMap.html#method.entry_ref) method on
[`HashMap`](struct.HashMap.html).

[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) and
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) on the borrowed
form of the map’s key type *must* match those for the key type. It also
require that key may be constructed from the borrowed form through the
[`From`](https://doc.rust-lang.org/std/convert/trait.From.html) trait.

## <a href="#examples" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{EntryRef, HashMap, OccupiedEntryRef};

let mut map = HashMap::new();
map.extend([("a".to_owned(), 10), ("b".into(), 20), ("c".into(), 30)]);
assert_eq!(map.len(), 3);

// Existing key (insert)
let key = String::from("a");
let entry: EntryRef<_, _, _, _> = map.entry_ref(&key);
let _raw_o: OccupiedEntryRef<_, _, _, _> = entry.insert(1);
assert_eq!(map.len(), 3);
// Nonexistent key (insert)
map.entry_ref("d").insert(4);

// Existing key (or_insert)
let v = map.entry_ref("b").or_insert(2);
assert_eq!(std::mem::replace(v, 2), 20);
// Nonexistent key (or_insert)
map.entry_ref("e").or_insert(5);

// Existing key (or_insert_with)
let v = map.entry_ref("c").or_insert_with(|| 3);
assert_eq!(std::mem::replace(v, 3), 30);
// Nonexistent key (or_insert_with)
map.entry_ref("f").or_insert_with(|| 6);

println!("Our HashMap: {:?}", map);

for (key, value) in ["a", "b", "c", "d", "e", "f"].into_iter().zip(1..=6) {
    assert_eq!(map[key], value)
}
assert_eq!(map.len(), 6);
```

</div>

</div>

## Variants<a href="#variants" class="anchor">§</a>

<div class="variants">

<div id="variant.Occupied" class="section variant">

<a href="#variant.Occupied" class="anchor">§</a>

### Occupied(<a href="struct.OccupiedEntryRef.html" class="struct"
title="struct hashbrown::hash_map::OccupiedEntryRef">OccupiedEntryRef</a>\<'a, 'b, K, Q, V, S, A\>)

</div>

<div class="docblock">

An occupied entry.

#### <a href="#examples-1" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{EntryRef, HashMap};
let mut map: HashMap<_, _> = [("a".to_owned(), 100), ("b".into(), 200)].into();

match map.entry_ref("a") {
    EntryRef::Vacant(_) => unreachable!(),
    EntryRef::Occupied(_) => { }
}
```

</div>

</div>

<div id="variant.Vacant" class="section variant">

<a href="#variant.Vacant" class="anchor">§</a>

### Vacant(<a href="struct.VacantEntryRef.html" class="struct"
title="struct hashbrown::hash_map::VacantEntryRef">VacantEntryRef</a>\<'a, 'b, K, Q, V, S, A\>)

</div>

<div class="docblock">

A vacant entry.

#### <a href="#examples-2" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{EntryRef, HashMap};
let mut map: HashMap<String, i32> = HashMap::new();

match map.entry_ref("a") {
    EntryRef::Occupied(_) => unreachable!(),
    EntryRef::Vacant(_) => { }
}
```

</div>

</div>

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-EntryRef%3C'a,+'b,+K,+Q,+V,+S,+A%3E" class="section impl">

<a href="../../src/hashbrown/map.rs.html#5595-5844"
class="src rightside">Source</a><a href="#impl-EntryRef%3C&#39;a,+&#39;b,+K,+Q,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, 'b, K, Q: ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, V, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="enum.EntryRef.html" class="enum"
title="enum hashbrown::hash_map::EntryRef">EntryRef</a>\<'a, 'b, K, Q, V, S, A\>

</div>

<div class="impl-items">

<div id="method.insert" class="section method">

<a href="../../src/hashbrown/map.rs.html#5609-5621"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert" class="fn">insert</a>(self, value: V) -\> <a href="struct.OccupiedEntryRef.html" class="struct"
title="struct hashbrown::hash_map::OccupiedEntryRef">OccupiedEntryRef</a>\<'a, 'b, K, Q, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'b Q</a>\>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="docblock">

Sets the value of the entry, and returns an OccupiedEntryRef.

##### <a href="#examples-3" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<String, u32> = HashMap::new();
let entry = map.entry_ref("horseyland").insert(37);

assert_eq!(entry.key(), "horseyland");
```

</div>

</div>

<div id="method.or_insert" class="section method">

<a href="../../src/hashbrown/map.rs.html#5642-5651"
class="src rightside">Source</a>

#### pub fn <a href="#method.or_insert" class="fn">or_insert</a>(self, default: V) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut V</a>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'b Q</a>\>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="docblock">

Ensures a value is in the entry by inserting the default if empty, and
returns a mutable reference to the value in the entry.

##### <a href="#examples-4" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<String, u32> = HashMap::new();

// nonexistent key
map.entry_ref("poneyland").or_insert(3);
assert_eq!(map["poneyland"], 3);

// existing key
*map.entry_ref("poneyland").or_insert(10) *= 2;
assert_eq!(map["poneyland"], 6);
```

</div>

</div>

<div id="method.or_insert_with" class="section method">

<a href="../../src/hashbrown/map.rs.html#5672-5681"
class="src rightside">Source</a>

#### pub fn <a href="#method.or_insert_with" class="fn">or_insert_with</a>\<F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnOnce.html"
class="trait" title="trait core::ops::function::FnOnce">FnOnce</a>() -\> V\>(self, default: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut V</a>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'b Q</a>\>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="docblock">

Ensures a value is in the entry by inserting the result of the default
function if empty, and returns a mutable reference to the value in the
entry.

##### <a href="#examples-5" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<String, u32> = HashMap::new();

// nonexistent key
map.entry_ref("poneyland").or_insert_with(|| 3);
assert_eq!(map["poneyland"], 3);

// existing key
*map.entry_ref("poneyland").or_insert_with(|| 10) *= 2;
assert_eq!(map["poneyland"], 6);
```

</div>

</div>

<div id="method.or_insert_with_key" class="section method">

<a href="../../src/hashbrown/map.rs.html#5706-5718"
class="src rightside">Source</a>

#### pub fn <a href="#method.or_insert_with_key" class="fn">or_insert_with_key</a>\<F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnOnce.html"
class="trait" title="trait core::ops::function::FnOnce">FnOnce</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> V\>(self, default: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut V</a>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<Q\> +
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'b Q</a>\>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="docblock">

Ensures a value is in the entry by inserting, if empty, the result of
the default function. This method allows for generating key-derived
values for insertion by providing the default function a reference to
the key that was moved during the `.entry_ref(key)` method call.

The reference to the moved key is provided so that cloning or copying
the key is unnecessary, unlike with `.or_insert_with(|| ... )`.

##### <a href="#examples-6" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<String, usize> = HashMap::new();

// nonexistent key
map.entry_ref("poneyland").or_insert_with_key(|key| key.chars().count());
assert_eq!(map["poneyland"], 9);

// existing key
*map.entry_ref("poneyland").or_insert_with_key(|key| key.chars().count() * 10) *= 2;
assert_eq!(map["poneyland"], 18);
```

</div>

</div>

<div id="method.key" class="section method">

<a href="../../src/hashbrown/map.rs.html#5735-5743"
class="src rightside">Source</a>

#### pub fn <a href="#method.key" class="fn">key</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<Q\>,

</div>

</div>

<div class="docblock">

Returns a reference to this entry’s key.

##### <a href="#examples-7" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<String, u32> = HashMap::new();
map.entry_ref("poneyland").or_insert(3);
// existing key
assert_eq!(map.entry_ref("poneyland").key(), "poneyland");
// nonexistent key
assert_eq!(map.entry_ref("horseland").key(), "horseland");
```

</div>

</div>

<div id="method.and_modify" class="section method">

<a href="../../src/hashbrown/map.rs.html#5766-5777"
class="src rightside">Source</a>

#### pub fn <a href="#method.and_modify" class="fn">and_modify</a>\<F\>(self, f: F) -\> Self

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnOnce.html"
class="trait" title="trait core::ops::function::FnOnce">FnOnce</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut V</a>),

</div>

</div>

<div class="docblock">

Provides in-place mutable access to an occupied entry before any
potential inserts into the map.

##### <a href="#examples-8" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<String, u32> = HashMap::new();

map.entry_ref("poneyland")
   .and_modify(|e| { *e += 1 })
   .or_insert(42);
assert_eq!(map["poneyland"], 42);

map.entry_ref("poneyland")
   .and_modify(|e| { *e += 1 })
   .or_insert(42);
assert_eq!(map["poneyland"], 43);
```

</div>

</div>

<div id="method.and_replace_entry_with" class="section method">

<a href="../../src/hashbrown/map.rs.html#5834-5843"
class="src rightside">Source</a>

#### pub fn <a href="#method.and_replace_entry_with"
class="fn">and_replace_entry_with</a>\<F\>(self, f: F) -\> Self

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnOnce.html"
class="trait" title="trait core::ops::function::FnOnce">FnOnce</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>, V) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<V\>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<Q\>,

</div>

</div>

<div class="docblock">

Provides shared access to the key and owned access to the value of an
occupied entry and allows to replace or remove it based on the value of
the returned option.

##### <a href="#examples-9" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use hashbrown::hash_map::EntryRef;

let mut map: HashMap<String, u32> = HashMap::new();

let entry = map
    .entry_ref("poneyland")
    .and_replace_entry_with(|_k, _v| panic!());

match entry {
    EntryRef::Vacant(e) => {
        assert_eq!(e.key(), "poneyland");
    }
    EntryRef::Occupied(_) => panic!(),
}

map.insert("poneyland".to_string(), 42);

let entry = map
    .entry_ref("poneyland")
    .and_replace_entry_with(|k, v| {
        assert_eq!(k, "poneyland");
        assert_eq!(v, 42);
        Some(v + 1)
    });

match entry {
    EntryRef::Occupied(e) => {
        assert_eq!(e.key(), "poneyland");
        assert_eq!(e.get(), &43);
    }
    EntryRef::Vacant(_) => panic!(),
}

assert_eq!(map["poneyland"], 43);

let entry = map
    .entry_ref("poneyland")
    .and_replace_entry_with(|_k, _v| None);

match entry {
    EntryRef::Vacant(e) => assert_eq!(e.key(), "poneyland"),
    EntryRef::Occupied(_) => panic!(),
}

assert!(!map.contains_key("poneyland"));
```

</div>

</div>

</div>

<div id="impl-EntryRef%3C'a,+'b,+K,+Q,+V,+S,+A%3E-1"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#5846-5877"
class="src rightside">Source</a><a href="#impl-EntryRef%3C&#39;a,+&#39;b,+K,+Q,+V,+S,+A%3E-1"
class="anchor">§</a>

### impl\<'a, 'b, K, Q: ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, V: <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="enum.EntryRef.html" class="enum"
title="enum hashbrown::hash_map::EntryRef">EntryRef</a>\<'a, 'b, K, Q, V, S, A\>

</div>

<div class="impl-items">

<div id="method.or_default" class="section method">

<a href="../../src/hashbrown/map.rs.html#5867-5876"
class="src rightside">Source</a>

#### pub fn <a href="#method.or_default" class="fn">or_default</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut V</a>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'b Q</a>\>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="docblock">

Ensures a value is in the entry by inserting the default value if empty,
and returns a mutable reference to the value in the entry.

##### <a href="#examples-10" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<String, Option<u32>> = HashMap::new();

// nonexistent key
map.entry_ref("poneyland").or_default();
assert_eq!(map["poneyland"], None);

map.insert("horseland".to_string(), Some(3));

// existing key
assert_eq!(map.entry_ref("horseland").or_default(), &mut Some(3));
```

</div>

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Debug-for-EntryRef%3C'_,+'_,+K,+Q,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#4356-4365"
class="src rightside">Source</a><a href="#impl-Debug-for-EntryRef%3C&#39;_,+&#39;_,+K,+Q,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<K: <a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<Q\>, Q: ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a> + <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, V: <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="enum.EntryRef.html" class="enum"
title="enum hashbrown::hash_map::EntryRef">EntryRef</a>\<'\_, '\_, K, Q, V, S, A\>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#4359-4364"
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

<div id="impl-Freeze-for-EntryRef%3C'a,+'b,+K,+Q,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Freeze-for-EntryRef%3C&#39;a,+&#39;b,+K,+Q,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, 'b, K, Q, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="enum.EntryRef.html" class="enum"
title="enum hashbrown::hash_map::EntryRef">EntryRef</a>\<'a, 'b, K, Q, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a>, Q:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div id="impl-RefUnwindSafe-for-EntryRef%3C'a,+'b,+K,+Q,+V,+S,+A%3E"
class="section impl">

<a
href="#impl-RefUnwindSafe-for-EntryRef%3C&#39;a,+&#39;b,+K,+Q,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, 'b, K, Q, V, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="enum.EntryRef.html" class="enum"
title="enum hashbrown::hash_map::EntryRef">EntryRef</a>\<'a, 'b, K, Q, V, S, A\>

<div class="where">

where K: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
S: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
Q: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, V: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
A: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,

</div>

</div>

<div id="impl-Send-for-EntryRef%3C'a,+'b,+K,+Q,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Send-for-EntryRef%3C&#39;a,+&#39;b,+K,+Q,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, 'b, K, Q, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="enum.EntryRef.html" class="enum"
title="enum hashbrown::hash_map::EntryRef">EntryRef</a>\<'a, 'b, K, Q, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, Q:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>,

</div>

</div>

<div id="impl-Sync-for-EntryRef%3C'a,+'b,+K,+Q,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Sync-for-EntryRef%3C&#39;a,+&#39;b,+K,+Q,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, 'b, K, Q, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="enum.EntryRef.html" class="enum"
title="enum hashbrown::hash_map::EntryRef">EntryRef</a>\<'a, 'b, K, Q, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, Q:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>,

</div>

</div>

<div id="impl-Unpin-for-EntryRef%3C'a,+'b,+K,+Q,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Unpin-for-EntryRef%3C&#39;a,+&#39;b,+K,+Q,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, 'b, K, Q, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="enum.EntryRef.html" class="enum"
title="enum hashbrown::hash_map::EntryRef">EntryRef</a>\<'a, 'b, K, Q, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>, Q:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div id="impl-UnwindSafe-for-EntryRef%3C'a,+'b,+K,+Q,+V,+S,+A%3E"
class="section impl">

<a
href="#impl-UnwindSafe-for-EntryRef%3C&#39;a,+&#39;b,+K,+Q,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, 'b, K, Q, V, S, A = Global\> \!<a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="enum.EntryRef.html" class="enum"
title="enum hashbrown::hash_map::EntryRef">EntryRef</a>\<'a, 'b, K, Q, V, S, A\>

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
