<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[hashbrown](../index.html)::[hash_map](index.html)

</div>

# Struct <span class="struct">OccupiedEntryRef</span> Copy item path

<span class="sub-heading"><a href="../../src/hashbrown/map.rs.html#4434-4439"
class="src">Source</a> </span>

</div>

``` rust
pub struct OccupiedEntryRef<'a, 'b, K, Q: ?Sized, V, S, A: Allocator + Clone = Global> { /* private fields */ }
```

Expand description

<div class="docblock">

A view into an occupied entry in a `HashMap`. It is part of the
[`EntryRef`](enum.EntryRef.html) enum.

## <a href="#examples" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{EntryRef, HashMap, OccupiedEntryRef};

let mut map = HashMap::new();
map.extend([("a".to_owned(), 10), ("b".into(), 20), ("c".into(), 30)]);

let key = String::from("a");
let _entry_o: OccupiedEntryRef<_, _, _, _> = map.entry_ref(&key).insert(100);
assert_eq!(map.len(), 3);

// Existing key (insert and update)
match map.entry_ref("a") {
    EntryRef::Vacant(_) => unreachable!(),
    EntryRef::Occupied(mut view) => {
        assert_eq!(view.get(), &100);
        let v = view.get_mut();
        *v *= 10;
        assert_eq!(view.insert(1111), 1000);
    }
}

assert_eq!(map["a"], 1111);
assert_eq!(map.len(), 3);

// Existing key (take)
match map.entry_ref("c") {
    EntryRef::Vacant(_) => unreachable!(),
    EntryRef::Occupied(view) => {
        assert_eq!(view.remove_entry(), ("c".to_owned(), 30));
    }
}
assert_eq!(map.get("c"), None);
assert_eq!(map.len(), 2);
```

</div>

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-OccupiedEntryRef%3C'a,+'b,+K,+Q,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#5879-6235"
class="src rightside">Source</a><a href="#impl-OccupiedEntryRef%3C&#39;a,+&#39;b,+K,+Q,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, 'b, K, Q: ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, V, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="struct.OccupiedEntryRef.html" class="struct"
title="struct hashbrown::hash_map::OccupiedEntryRef">OccupiedEntryRef</a>\<'a, 'b, K, Q, V, S, A\>

</div>

<div class="impl-items">

<div id="method.key" class="section method">

<a href="../../src/hashbrown/map.rs.html#5896-5901"
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

Gets a reference to the key in the entry.

##### <a href="#examples-1" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{EntryRef, HashMap};

let mut map: HashMap<String, u32> = HashMap::new();
map.entry_ref("poneyland").or_insert(12);

match map.entry_ref("poneyland") {
    EntryRef::Vacant(_) => panic!(),
    EntryRef::Occupied(entry) => assert_eq!(entry.key(), "poneyland"),
}
```

</div>

</div>

<div id="method.remove_entry" class="section method">

<a href="../../src/hashbrown/map.rs.html#5929-5931"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove_entry" class="fn">remove_entry</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(K, V)</a>

</div>

<div class="docblock">

Take the ownership of the key and value from the map. Keeps the
allocated memory for reuse.

##### <a href="#examples-2" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use hashbrown::hash_map::EntryRef;

let mut map: HashMap<String, u32> = HashMap::new();
// The map is empty
assert!(map.is_empty() && map.capacity() == 0);

map.entry_ref("poneyland").or_insert(12);
let capacity_before_remove = map.capacity();

if let EntryRef::Occupied(o) = map.entry_ref("poneyland") {
    // We delete the entry from the map.
    assert_eq!(o.remove_entry(), ("poneyland".to_owned(), 12));
}

assert_eq!(map.contains_key("poneyland"), false);
// Now map hold none elements but capacity is equal to the old one
assert!(map.len() == 0 && map.capacity() == capacity_before_remove);
```

</div>

</div>

<div id="method.get" class="section method">

<a href="../../src/hashbrown/map.rs.html#5950-5952"
class="src rightside">Source</a>

#### pub fn <a href="#method.get" class="fn">get</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;V</a>

</div>

<div class="docblock">

Gets a reference to the value in the entry.

##### <a href="#examples-3" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use hashbrown::hash_map::EntryRef;

let mut map: HashMap<String, u32> = HashMap::new();
map.entry_ref("poneyland").or_insert(12);

match map.entry_ref("poneyland") {
    EntryRef::Vacant(_) => panic!(),
    EntryRef::Occupied(entry) => assert_eq!(entry.get(), &12),
}
```

</div>

</div>

<div id="method.get_mut" class="section method">

<a href="../../src/hashbrown/map.rs.html#5982-5984"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_mut" class="fn">get_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut V</a>

</div>

<div class="docblock">

Gets a mutable reference to the value in the entry.

If you need a reference to the `OccupiedEntryRef` which may outlive the
destruction of the `EntryRef` value, see [`into_mut`](#method.into_mut).

##### <a href="#examples-4" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use hashbrown::hash_map::EntryRef;

let mut map: HashMap<String, u32> = HashMap::new();
map.entry_ref("poneyland").or_insert(12);

assert_eq!(map["poneyland"], 12);
if let EntryRef::Occupied(mut o) = map.entry_ref("poneyland") {
    *o.get_mut() += 10;
    assert_eq!(*o.get(), 22);

    // We can use the same Entry multiple times.
    *o.get_mut() += 2;
}

assert_eq!(map["poneyland"], 24);
```

</div>

</div>

<div id="method.into_mut" class="section method">

<a href="../../src/hashbrown/map.rs.html#6011-6013"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_mut" class="fn">into_mut</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut V</a>

</div>

<div class="docblock">

Converts the OccupiedEntryRef into a mutable reference to the value in
the entry with a lifetime bound to the map itself.

If you need multiple references to the `OccupiedEntryRef`, see
[`get_mut`](#method.get_mut).

##### <a href="#examples-5" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{EntryRef, HashMap};

let mut map: HashMap<String, u32> = HashMap::new();
map.entry_ref("poneyland").or_insert(12);

let value: &mut u32;
match map.entry_ref("poneyland") {
    EntryRef::Occupied(entry) => value = entry.into_mut(),
    EntryRef::Vacant(_) => panic!(),
}
*value += 10;

assert_eq!(map["poneyland"], 22);
```

</div>

</div>

<div id="method.insert" class="section method">

<a href="../../src/hashbrown/map.rs.html#6033-6035"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert" class="fn">insert</a>(&mut self, value: V) -\> V

</div>

<div class="docblock">

Sets the value of the entry, and returns the entry’s old value.

##### <a href="#examples-6" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use hashbrown::hash_map::EntryRef;

let mut map: HashMap<String, u32> = HashMap::new();
map.entry_ref("poneyland").or_insert(12);

if let EntryRef::Occupied(mut o) = map.entry_ref("poneyland") {
    assert_eq!(o.insert(15), 12);
}

assert_eq!(map["poneyland"], 15);
```

</div>

</div>

<div id="method.remove" class="section method">

<a href="../../src/hashbrown/map.rs.html#6062-6064"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove" class="fn">remove</a>(self) -\> V

</div>

<div class="docblock">

Takes the value out of the entry, and returns it. Keeps the allocated
memory for reuse.

##### <a href="#examples-7" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use hashbrown::hash_map::EntryRef;

let mut map: HashMap<String, u32> = HashMap::new();
// The map is empty
assert!(map.is_empty() && map.capacity() == 0);

map.entry_ref("poneyland").or_insert(12);
let capacity_before_remove = map.capacity();

if let EntryRef::Occupied(o) = map.entry_ref("poneyland") {
    assert_eq!(o.remove(), 12);
}

assert_eq!(map.contains_key("poneyland"), false);
// Now map hold none elements but capacity is equal to the old one
assert!(map.len() == 0 && map.capacity() == capacity_before_remove);
```

</div>

</div>

<div id="method.replace_entry" class="section method">

<a href="../../src/hashbrown/map.rs.html#6097-6107"
class="src rightside">Source</a>

#### pub fn <a href="#method.replace_entry" class="fn">replace_entry</a>(self, value: V) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(K, V)</a>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'b Q</a>\>,

</div>

</div>

<div class="docblock">

Replaces the entry, returning the old key and value. The new key in the
hash map will be the key used to create this entry.

##### <a href="#panics" class="doc-anchor">§</a>Panics

Will panic if this OccupiedEntry was created through
[`EntryRef::insert`](enum.EntryRef.html#method.insert "method hashbrown::hash_map::EntryRef::insert").

##### <a href="#examples-8" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{EntryRef, HashMap};
use std::rc::Rc;

let mut map: HashMap<Rc<str>, u32> = HashMap::new();
let key: Rc<str> = Rc::from("Stringthing");

map.insert(key.clone(), 15);
assert_eq!(Rc::strong_count(&key), 2);

match map.entry_ref("Stringthing") {
    EntryRef::Occupied(entry) => {
        let (old_key, old_value): (Rc<str>, u32) = entry.replace_entry(16);
        assert!(Rc::ptr_eq(&key, &old_key) && old_value == 15);
    }
    EntryRef::Vacant(_) => panic!(),
}

assert_eq!(Rc::strong_count(&key), 1);
assert_eq!(map["Stringthing"], 16);
```

</div>

</div>

<div id="method.replace_key" class="section method">

<a href="../../src/hashbrown/map.rs.html#6148-6154"
class="src rightside">Source</a>

#### pub fn <a href="#method.replace_key" class="fn">replace_key</a>(self) -\> K

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'b Q</a>\>,

</div>

</div>

<div class="docblock">

Replaces the key in the hash map with the key used to create this entry.

##### <a href="#panics-1" class="doc-anchor">§</a>Panics

Will panic if this OccupiedEntry was created through
[`Entry::insert`](enum.Entry.html#method.insert "method hashbrown::hash_map::Entry::insert").

##### <a href="#examples-9" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{EntryRef, HashMap};
use std::rc::Rc;

let mut map: HashMap<Rc<str>, usize> = HashMap::with_capacity(6);
let mut keys: Vec<Rc<str>> = Vec::with_capacity(6);

for (value, key) in ["a", "b", "c", "d", "e", "f"].into_iter().enumerate() {
    let rc_key: Rc<str> = Rc::from(key);
    keys.push(rc_key.clone());
    map.insert(rc_key.clone(), value);
}

assert!(keys.iter().all(|key| Rc::strong_count(key) == 2));

// It doesn't matter that we kind of use a vector with the same keys,
// because all keys will be newly created from the references
reclaim_memory(&mut map, &keys);

assert!(keys.iter().all(|key| Rc::strong_count(key) == 1));

fn reclaim_memory(map: &mut HashMap<Rc<str>, usize>, keys: &[Rc<str>]) {
    for key in keys {
        if let EntryRef::Occupied(entry) = map.entry_ref(key.as_ref()) {
        /// Replaces the entry's key with our version of it in `keys`.
            entry.replace_key();
        }
    }
}
```

</div>

</div>

<div id="method.replace_entry_with" class="section method">

<a href="../../src/hashbrown/map.rs.html#6205-6234"
class="src rightside">Source</a>

#### pub fn <a href="#method.replace_entry_with" class="fn">replace_entry_with</a>\<F\>(self, f: F) -\> <a href="enum.EntryRef.html" class="enum"
title="enum hashbrown::hash_map::EntryRef">EntryRef</a>\<'a, 'b, K, Q, V, S, A\>

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

Provides shared access to the key and owned access to the value of the
entry and allows to replace or remove it based on the value of the
returned option.

##### <a href="#examples-10" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use hashbrown::hash_map::EntryRef;

let mut map: HashMap<String, u32> = HashMap::new();
map.insert("poneyland".to_string(), 42);

let entry = match map.entry_ref("poneyland") {
    EntryRef::Occupied(e) => {
        e.replace_entry_with(|k, v| {
            assert_eq!(k, "poneyland");
            assert_eq!(v, 42);
            Some(v + 1)
        })
    }
    EntryRef::Vacant(_) => panic!(),
};

match entry {
    EntryRef::Occupied(e) => {
        assert_eq!(e.key(), "poneyland");
        assert_eq!(e.get(), &43);
    }
    EntryRef::Vacant(_) => panic!(),
}

assert_eq!(map["poneyland"], 43);

let entry = match map.entry_ref("poneyland") {
    EntryRef::Occupied(e) => e.replace_entry_with(|_k, _v| None),
    EntryRef::Vacant(_) => panic!(),
};

match entry {
    EntryRef::Vacant(e) => {
        assert_eq!(e.key(), "poneyland");
    }
    EntryRef::Occupied(_) => panic!(),
}

assert!(!map.contains_key("poneyland"));
```

</div>

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Debug-for-OccupiedEntryRef%3C'_,+'_,+K,+Q,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#4460-4469"
class="src rightside">Source</a><a
href="#impl-Debug-for-OccupiedEntryRef%3C&#39;_,+&#39;_,+K,+Q,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<K: <a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<Q\>, Q: ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a> + <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, V: <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.OccupiedEntryRef.html" class="struct"
title="struct hashbrown::hash_map::OccupiedEntryRef">OccupiedEntryRef</a>\<'\_, '\_, K, Q, V, S, A\>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#4463-4468"
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

<div id="impl-Send-for-OccupiedEntryRef%3C'a,+'b,+K,+Q,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#4441-4449"
class="src rightside">Source</a><a
href="#impl-Send-for-OccupiedEntryRef%3C&#39;a,+&#39;b,+K,+Q,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, 'b, K, Q, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.OccupiedEntryRef.html" class="struct"
title="struct hashbrown::hash_map::OccupiedEntryRef">OccupiedEntryRef</a>\<'a, 'b, K, Q, V, S, A\>

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
class="trait" title="trait core::marker::Send">Send</a> + Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div id="impl-Sync-for-OccupiedEntryRef%3C'a,+'b,+K,+Q,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#4450-4458"
class="src rightside">Source</a><a
href="#impl-Sync-for-OccupiedEntryRef%3C&#39;a,+&#39;b,+K,+Q,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, 'b, K, Q, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.OccupiedEntryRef.html" class="struct"
title="struct hashbrown::hash_map::OccupiedEntryRef">OccupiedEntryRef</a>\<'a, 'b, K, Q, V, S, A\>

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
class="trait" title="trait core::marker::Sync">Sync</a> + Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-OccupiedEntryRef%3C'a,+'b,+K,+Q,+V,+S,+A%3E"
class="section impl">

<a
href="#impl-Freeze-for-OccupiedEntryRef%3C&#39;a,+&#39;b,+K,+Q,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, 'b, K, Q, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.OccupiedEntryRef.html" class="struct"
title="struct hashbrown::hash_map::OccupiedEntryRef">OccupiedEntryRef</a>\<'a, 'b, K, Q, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a>, Q:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div id="impl-RefUnwindSafe-for-OccupiedEntryRef%3C'a,+'b,+K,+Q,+V,+S,+A%3E"
class="section impl">

<a
href="#impl-RefUnwindSafe-for-OccupiedEntryRef%3C&#39;a,+&#39;b,+K,+Q,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, 'b, K, Q, V, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.OccupiedEntryRef.html" class="struct"
title="struct hashbrown::hash_map::OccupiedEntryRef">OccupiedEntryRef</a>\<'a, 'b, K, Q, V, S, A\>

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

<div id="impl-Unpin-for-OccupiedEntryRef%3C'a,+'b,+K,+Q,+V,+S,+A%3E"
class="section impl">

<a
href="#impl-Unpin-for-OccupiedEntryRef%3C&#39;a,+&#39;b,+K,+Q,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, 'b, K, Q, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.OccupiedEntryRef.html" class="struct"
title="struct hashbrown::hash_map::OccupiedEntryRef">OccupiedEntryRef</a>\<'a, 'b, K, Q, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>, Q:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div id="impl-UnwindSafe-for-OccupiedEntryRef%3C'a,+'b,+K,+Q,+V,+S,+A%3E"
class="section impl">

<a
href="#impl-UnwindSafe-for-OccupiedEntryRef%3C&#39;a,+&#39;b,+K,+Q,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, 'b, K, Q, V, S, A = Global\> \!<a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.OccupiedEntryRef.html" class="struct"
title="struct hashbrown::hash_map::OccupiedEntryRef">OccupiedEntryRef</a>\<'a, 'b, K, Q, V, S, A\>

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
