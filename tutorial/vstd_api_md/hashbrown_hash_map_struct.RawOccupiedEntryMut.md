<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[hashbrown](../index.html)::[hash_map](index.html)

</div>

# Struct <span class="struct">RawOccupiedEntryMut</span> Copy item path

<span class="sub-heading"><a href="../../src/hashbrown/map.rs.html#2973-2977"
class="src">Source</a> </span>

</div>

``` rust
pub struct RawOccupiedEntryMut<'a, K, V, S, A: Allocator + Clone = Global> { /* private fields */ }
```

Expand description

<div class="docblock">

A view into an occupied entry in a `HashMap`. It is part of the
[`RawEntryMut`](enum.RawEntryMut.html) enum.

## <a href="#examples" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use core::hash::{BuildHasher, Hash};
use hashbrown::hash_map::{HashMap, RawEntryMut, RawOccupiedEntryMut};

let mut map = HashMap::new();
map.extend([("a", 10), ("b", 20), ("c", 30)]);

fn compute_hash<K: Hash + ?Sized, S: BuildHasher>(hash_builder: &S, key: &K) -> u64 {
    use core::hash::Hasher;
    let mut state = hash_builder.build_hasher();
    key.hash(&mut state);
    state.finish()
}

let _raw_o: RawOccupiedEntryMut<_, _, _> = map.raw_entry_mut().from_key(&"a").insert("a", 100);
assert_eq!(map.len(), 3);

// Existing key (insert and update)
match map.raw_entry_mut().from_key(&"a") {
    RawEntryMut::Vacant(_) => unreachable!(),
    RawEntryMut::Occupied(mut view) => {
        assert_eq!(view.get(), &100);
        let v = view.get_mut();
        let new_v = (*v) * 10;
        *v = new_v;
        assert_eq!(view.insert(1111), 1000);
    }
}

assert_eq!(map[&"a"], 1111);
assert_eq!(map.len(), 3);

// Existing key (take)
let hash = compute_hash(map.hasher(), &"c");
match map.raw_entry_mut().from_key_hashed_nocheck(hash, &"c") {
    RawEntryMut::Vacant(_) => unreachable!(),
    RawEntryMut::Occupied(view) => {
        assert_eq!(view.remove_entry(), ("c", 30));
    }
}
assert_eq!(map.raw_entry().from_key(&"c"), None);
assert_eq!(map.len(), 2);

let hash = compute_hash(map.hasher(), &"b");
match map.raw_entry_mut().from_hash(hash, |q| *q == "b") {
    RawEntryMut::Vacant(_) => unreachable!(),
    RawEntryMut::Occupied(view) => {
        assert_eq!(view.remove_entry(), ("b", 20));
    }
}
assert_eq!(map.get(&"b"), None);
assert_eq!(map.len(), 1);
```

</div>

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-RawOccupiedEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#3486-3883"
class="src rightside">Source</a><a href="#impl-RawOccupiedEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="struct.RawOccupiedEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawOccupiedEntryMut">RawOccupiedEntryMut</a>\<'a, K, V, S, A\>

</div>

<div class="impl-items">

<div id="method.key" class="section method">

<a href="../../src/hashbrown/map.rs.html#3502-3504"
class="src rightside">Source</a>

#### pub fn <a href="#method.key" class="fn">key</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;K</a>

</div>

<div class="docblock">

Gets a reference to the key in the entry.

##### <a href="#examples-1" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{HashMap, RawEntryMut};

let mut map: HashMap<&str, u32> = [("a", 100), ("b", 200)].into();

match map.raw_entry_mut().from_key(&"a") {
    RawEntryMut::Vacant(_) => panic!(),
    RawEntryMut::Occupied(o) => assert_eq!(o.key(), &"a")
}
```

</div>

</div>

<div id="method.key_mut" class="section method">

<a href="../../src/hashbrown/map.rs.html#3533-3535"
class="src rightside">Source</a>

#### pub fn <a href="#method.key_mut" class="fn">key_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut K</a>

</div>

<div class="docblock">

Gets a mutable reference to the key in the entry.

##### <a href="#examples-2" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{HashMap, RawEntryMut};
use std::rc::Rc;

let key_one = Rc::new("a");
let key_two = Rc::new("a");

let mut map: HashMap<Rc<&str>, u32> = HashMap::new();
map.insert(key_one.clone(), 10);

assert_eq!(map[&key_one], 10);
assert!(Rc::strong_count(&key_one) == 2 && Rc::strong_count(&key_two) == 1);

match map.raw_entry_mut().from_key(&key_one) {
    RawEntryMut::Vacant(_) => panic!(),
    RawEntryMut::Occupied(mut o) => {
        *o.key_mut() = key_two.clone();
    }
}
assert_eq!(map[&key_two], 10);
assert!(Rc::strong_count(&key_one) == 1 && Rc::strong_count(&key_two) == 2);
```

</div>

</div>

<div id="method.into_key" class="section method">

<a href="../../src/hashbrown/map.rs.html#3567-3569"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_key" class="fn">into_key</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut K</a>

</div>

<div class="docblock">

Converts the entry into a mutable reference to the key in the entry with
a lifetime bound to the map itself.

##### <a href="#examples-3" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{HashMap, RawEntryMut};
use std::rc::Rc;

let key_one = Rc::new("a");
let key_two = Rc::new("a");

let mut map: HashMap<Rc<&str>, u32> = HashMap::new();
map.insert(key_one.clone(), 10);

assert_eq!(map[&key_one], 10);
assert!(Rc::strong_count(&key_one) == 2 && Rc::strong_count(&key_two) == 1);

let inside_key: &mut Rc<&str>;

match map.raw_entry_mut().from_key(&key_one) {
    RawEntryMut::Vacant(_) => panic!(),
    RawEntryMut::Occupied(o) => inside_key = o.into_key(),
}
*inside_key = key_two.clone();

assert_eq!(map[&key_two], 10);
assert!(Rc::strong_count(&key_one) == 1 && Rc::strong_count(&key_two) == 2);
```

</div>

</div>

<div id="method.get" class="section method">

<a href="../../src/hashbrown/map.rs.html#3586-3588"
class="src rightside">Source</a>

#### pub fn <a href="#method.get" class="fn">get</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;V</a>

</div>

<div class="docblock">

Gets a reference to the value in the entry.

##### <a href="#examples-4" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{HashMap, RawEntryMut};

let mut map: HashMap<&str, u32> = [("a", 100), ("b", 200)].into();

match map.raw_entry_mut().from_key(&"a") {
    RawEntryMut::Vacant(_) => panic!(),
    RawEntryMut::Occupied(o) => assert_eq!(o.get(), &100),
}
```

</div>

</div>

<div id="method.into_mut" class="section method">

<a href="../../src/hashbrown/map.rs.html#3611-3613"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_mut" class="fn">into_mut</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut V</a>

</div>

<div class="docblock">

Converts the OccupiedEntry into a mutable reference to the value in the
entry with a lifetime bound to the map itself.

##### <a href="#examples-5" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{HashMap, RawEntryMut};

let mut map: HashMap<&str, u32> = [("a", 100), ("b", 200)].into();

let value: &mut u32;

match map.raw_entry_mut().from_key(&"a") {
    RawEntryMut::Vacant(_) => panic!(),
    RawEntryMut::Occupied(o) => value = o.into_mut(),
}
*value += 900;

assert_eq!(map[&"a"], 1000);
```

</div>

</div>

<div id="method.get_mut" class="section method">

<a href="../../src/hashbrown/map.rs.html#3632-3634"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_mut" class="fn">get_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut V</a>

</div>

<div class="docblock">

Gets a mutable reference to the value in the entry.

##### <a href="#examples-6" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{HashMap, RawEntryMut};

let mut map: HashMap<&str, u32> = [("a", 100), ("b", 200)].into();

match map.raw_entry_mut().from_key(&"a") {
    RawEntryMut::Vacant(_) => panic!(),
    RawEntryMut::Occupied(mut o) => *o.get_mut() += 900,
}

assert_eq!(map[&"a"], 1000);
```

</div>

</div>

<div id="method.get_key_value" class="section method">

<a href="../../src/hashbrown/map.rs.html#3651-3656"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_key_value" class="fn">get_key_value</a>(&self) -\> (<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;K</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;V</a>)

</div>

<div class="docblock">

Gets a reference to the key and value in the entry.

##### <a href="#examples-7" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{HashMap, RawEntryMut};

let mut map: HashMap<&str, u32> = [("a", 100), ("b", 200)].into();

match map.raw_entry_mut().from_key(&"a") {
    RawEntryMut::Vacant(_) => panic!(),
    RawEntryMut::Occupied(o) => assert_eq!(o.get_key_value(), (&"a", &100)),
}
```

</div>

</div>

<div id="method.get_key_value_mut" class="section method">

<a href="../../src/hashbrown/map.rs.html#3687-3692"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_key_value_mut" class="fn">get_key_value_mut</a>(&mut self) -\> (<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut K</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut V</a>)

</div>

<div class="docblock">

Gets a mutable reference to the key and value in the entry.

##### <a href="#examples-8" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{HashMap, RawEntryMut};
use std::rc::Rc;

let key_one = Rc::new("a");
let key_two = Rc::new("a");

let mut map: HashMap<Rc<&str>, u32> = HashMap::new();
map.insert(key_one.clone(), 10);

assert_eq!(map[&key_one], 10);
assert!(Rc::strong_count(&key_one) == 2 && Rc::strong_count(&key_two) == 1);

match map.raw_entry_mut().from_key(&key_one) {
    RawEntryMut::Vacant(_) => panic!(),
    RawEntryMut::Occupied(mut o) => {
        let (inside_key, inside_value) = o.get_key_value_mut();
        *inside_key = key_two.clone();
        *inside_value = 100;
    }
}
assert_eq!(map[&key_two], 100);
assert!(Rc::strong_count(&key_one) == 1 && Rc::strong_count(&key_two) == 2);
```

</div>

</div>

<div id="method.into_key_value" class="section method">

<a href="../../src/hashbrown/map.rs.html#3728-3733"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_key_value" class="fn">into_key_value</a>(self) -\> (<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut K</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut V</a>)

</div>

<div class="docblock">

Converts the OccupiedEntry into a mutable reference to the key and value
in the entry with a lifetime bound to the map itself.

##### <a href="#examples-9" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{HashMap, RawEntryMut};
use std::rc::Rc;

let key_one = Rc::new("a");
let key_two = Rc::new("a");

let mut map: HashMap<Rc<&str>, u32> = HashMap::new();
map.insert(key_one.clone(), 10);

assert_eq!(map[&key_one], 10);
assert!(Rc::strong_count(&key_one) == 2 && Rc::strong_count(&key_two) == 1);

let inside_key: &mut Rc<&str>;
let inside_value: &mut u32;
match map.raw_entry_mut().from_key(&key_one) {
    RawEntryMut::Vacant(_) => panic!(),
    RawEntryMut::Occupied(o) => {
        let tuple = o.into_key_value();
        inside_key = tuple.0;
        inside_value = tuple.1;
    }
}
*inside_key = key_two.clone();
*inside_value = 100;
assert_eq!(map[&key_two], 100);
assert!(Rc::strong_count(&key_one) == 1 && Rc::strong_count(&key_two) == 2);
```

</div>

</div>

<div id="method.insert" class="section method">

<a href="../../src/hashbrown/map.rs.html#3752-3754"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert" class="fn">insert</a>(&mut self, value: V) -\> V

</div>

<div class="docblock">

Sets the value of the entry, and returns the entry’s old value.

##### <a href="#examples-10" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{HashMap, RawEntryMut};

let mut map: HashMap<&str, u32> = [("a", 100), ("b", 200)].into();

match map.raw_entry_mut().from_key(&"a") {
    RawEntryMut::Vacant(_) => panic!(),
    RawEntryMut::Occupied(mut o) => assert_eq!(o.insert(1000), 100),
}

assert_eq!(map[&"a"], 1000);
```

</div>

</div>

<div id="method.insert_key" class="section method">

<a href="../../src/hashbrown/map.rs.html#3784-3786"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert_key" class="fn">insert_key</a>(&mut self, key: K) -\> K

</div>

<div class="docblock">

Sets the value of the entry, and returns the entry’s old value.

##### <a href="#examples-11" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{HashMap, RawEntryMut};
use std::rc::Rc;

let key_one = Rc::new("a");
let key_two = Rc::new("a");

let mut map: HashMap<Rc<&str>, u32> = HashMap::new();
map.insert(key_one.clone(), 10);

assert_eq!(map[&key_one], 10);
assert!(Rc::strong_count(&key_one) == 2 && Rc::strong_count(&key_two) == 1);

match map.raw_entry_mut().from_key(&key_one) {
    RawEntryMut::Vacant(_) => panic!(),
    RawEntryMut::Occupied(mut o) => {
        let old_key = o.insert_key(key_two.clone());
        assert!(Rc::ptr_eq(&old_key, &key_one));
    }
}
assert_eq!(map[&key_two], 10);
assert!(Rc::strong_count(&key_one) == 1 && Rc::strong_count(&key_two) == 2);
```

</div>

</div>

<div id="method.remove" class="section method">

<a href="../../src/hashbrown/map.rs.html#3804-3806"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove" class="fn">remove</a>(self) -\> V

</div>

<div class="docblock">

Takes the value out of the entry, and returns it.

##### <a href="#examples-12" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{HashMap, RawEntryMut};

let mut map: HashMap<&str, u32> = [("a", 100), ("b", 200)].into();

match map.raw_entry_mut().from_key(&"a") {
    RawEntryMut::Vacant(_) => panic!(),
    RawEntryMut::Occupied(o) => assert_eq!(o.remove(), 100),
}
assert_eq!(map.get(&"a"), None);
```

</div>

</div>

<div id="method.remove_entry" class="section method">

<a href="../../src/hashbrown/map.rs.html#3824-3826"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove_entry" class="fn">remove_entry</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(K, V)</a>

</div>

<div class="docblock">

Take the ownership of the key and value from the map.

##### <a href="#examples-13" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{HashMap, RawEntryMut};

let mut map: HashMap<&str, u32> = [("a", 100), ("b", 200)].into();

match map.raw_entry_mut().from_key(&"a") {
    RawEntryMut::Vacant(_) => panic!(),
    RawEntryMut::Occupied(o) => assert_eq!(o.remove_entry(), ("a", 100)),
}
assert_eq!(map.get(&"a"), None);
```

</div>

</div>

<div id="method.replace_entry_with" class="section method">

<a href="../../src/hashbrown/map.rs.html#3862-3882"
class="src rightside">Source</a>

#### pub fn <a href="#method.replace_entry_with" class="fn">replace_entry_with</a>\<F\>(self, f: F) -\> <a href="enum.RawEntryMut.html" class="enum"
title="enum hashbrown::hash_map::RawEntryMut">RawEntryMut</a>\<'a, K, V, S, A\>

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

Provides shared access to the key and owned access to the value of the
entry and allows to replace or remove it based on the value of the
returned option.

##### <a href="#examples-14" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::{HashMap, RawEntryMut};

let mut map: HashMap<&str, u32> = [("a", 100), ("b", 200)].into();

let raw_entry = match map.raw_entry_mut().from_key(&"a") {
    RawEntryMut::Vacant(_) => panic!(),
    RawEntryMut::Occupied(o) => o.replace_entry_with(|k, v| {
        assert_eq!(k, &"a");
        assert_eq!(v, 100);
        Some(v + 900)
    }),
};
let raw_entry = match raw_entry {
    RawEntryMut::Vacant(_) => panic!(),
    RawEntryMut::Occupied(o) => o.replace_entry_with(|k, v| {
        assert_eq!(k, &"a");
        assert_eq!(v, 1000);
        None
    }),
};
match raw_entry {
    RawEntryMut::Vacant(_) => { },
    RawEntryMut::Occupied(_) => panic!(),
};
assert_eq!(map.get(&"a"), None);
```

</div>

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Debug-for-RawOccupiedEntryMut%3C'_,+K,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#4046-4053"
class="src rightside">Source</a><a href="#impl-Debug-for-RawOccupiedEntryMut%3C&#39;_,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<K: <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, V: <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.RawOccupiedEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawOccupiedEntryMut">RawOccupiedEntryMut</a>\<'\_, K, V, S, A\>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#4047-4052"
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

<div id="impl-Send-for-RawOccupiedEntryMut%3C'_,+K,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#2979-2986"
class="src rightside">Source</a><a href="#impl-Send-for-RawOccupiedEntryMut%3C&#39;_,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.RawOccupiedEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawOccupiedEntryMut">RawOccupiedEntryMut</a>\<'\_, K, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, V:
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

<div id="impl-Sync-for-RawOccupiedEntryMut%3C'_,+K,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#2987-2994"
class="src rightside">Source</a><a href="#impl-Sync-for-RawOccupiedEntryMut%3C&#39;_,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.RawOccupiedEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawOccupiedEntryMut">RawOccupiedEntryMut</a>\<'\_, K, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, V:
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

<div id="impl-Freeze-for-RawOccupiedEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Freeze-for-RawOccupiedEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.RawOccupiedEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawOccupiedEntryMut">RawOccupiedEntryMut</a>\<'a, K, V, S, A\>

</div>

<div id="impl-RefUnwindSafe-for-RawOccupiedEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a
href="#impl-RefUnwindSafe-for-RawOccupiedEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.RawOccupiedEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawOccupiedEntryMut">RawOccupiedEntryMut</a>\<'a, K, V, S, A\>

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

<div id="impl-Unpin-for-RawOccupiedEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a href="#impl-Unpin-for-RawOccupiedEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.RawOccupiedEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawOccupiedEntryMut">RawOccupiedEntryMut</a>\<'a, K, V, S, A\>

</div>

<div id="impl-UnwindSafe-for-RawOccupiedEntryMut%3C'a,+K,+V,+S,+A%3E"
class="section impl">

<a
href="#impl-UnwindSafe-for-RawOccupiedEntryMut%3C&#39;a,+K,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A = Global\> \!<a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.RawOccupiedEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawOccupiedEntryMut">RawOccupiedEntryMut</a>\<'a, K, V, S, A\>

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
