<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../../index.html)::[tokens](../index.html)

</div>

# Module map Copy item path

<span class="sub-heading"><a href="../../../src/vstd/tokens/map.rs.html#1-1676"
class="src">Source</a> </span>

</div>

Expand description

<div class="docblock">

Maps that support ownership of keys

- [`GhostMapAuth<K, V>`](struct.GhostMapAuth.html "struct vstd::tokens::map::GhostMapAuth")
  represents authoritative ownership of the entire map;
- [`GhostSubmap<K, V>`](struct.GhostSubmap.html "struct vstd::tokens::map::GhostSubmap")
  represents client ownership of a submap;
- [`GhostPersistentSubmap<K, V>`](struct.GhostPersistentSubmap.html "struct vstd::tokens::map::GhostPersistentSubmap")
  represents duplicable client knowledge of a submap which will never
  change;
- [`GhostPointsTo<K, V>`](struct.GhostPointsTo.html "struct vstd::tokens::map::GhostPointsTo")
  represents client ownership of a single key-value pair.
- [`GhostPersistentPointsTo<K, V>`](struct.GhostPersistentPointsTo.html "struct vstd::tokens::map::GhostPersistentPointsTo")
  represents duplicable client knowledge of a single key-value pair
  which will never change.

Updating the authoritative `GhostMapAuth<K, V>` requires a
`GhostSubmap<K, V>` containing the keys being updated.

`GhostSubmap<K, V>`s can be combined or split. Whenever a
`GhostSubmap<K, V>` can be used, we can instead use a
`GhostPointsTo<K, V>` (but not vice-versa).

`GhostPersistentSubmap<K, V>`s can be combined or split. Whenever a
`GhostPersistentSubmap<K, V>` can be used, we can instead use a
`GhostPersistentPointsTo<K, V>` (but not vice-versa).

#### <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
fn example_use() {
    let tracked (mut auth, mut sub) = GhostMapAuth::new(map![1u8 => 1u64, 2u8 => 2u64, 3u8 => 3u64]);

    // Allocate some more keys in the auth map, receiving a new submap.
    let tracked sub2 = auth.insert_map(map![4u8 => 4u64, 5u8 => 5u64]);
    proof { sub.combine(sub2); }

    // Allocate a single key in the auth map, receiving a points to
    let tracked pt1 = auth.insert(6u8, 6u64);
    proof { sub.combine_points_to(pt1); }

    // Delete some keys in the auth map, by returning corresponding submap.
    let tracked sub3 = sub.split(set![3u8, 4u8]);
    proof { auth.delete(sub3); }

    // Split the submap into a points to and a submap
    let tracked pt2 = sub.split_points_to(1u8);
    let tracked sub4 = sub.split(set![5u8, 6u8]);

    // In general, we might need to call agree() to establish the fact that
    // a points-to/submap has the same values as the auth map.  Here, Verus
    // doesn't need agree because it can track where both the auth, points-to
    // and submap came from.
    proof { sub.agree(&auth); }
    proof { pt2.agree(&auth); }
    proof { sub4.agree(&auth); }

    assert(pt2.key() == 1u8);
    assert(pt2.value() == auth[1u8]);
    assert(sub4[5u8] == auth[5u8]);
    assert(sub4[6u8] == auth[6u8]);
    assert(sub[2u8] == auth[2u8]);

    // Update keys using ownership of submaps.
    proof { sub.update(&mut auth, map![2u8 => 22u64]); }
    proof { pt2.update(&mut auth, 11u64); }
    proof { sub4.update(&mut auth, map![5u8 => 55u64, 6u8 => 66u8]); }
    assert(auth[1u8] == 11u64);
    assert(auth[2u8] == 22u64);
    assert(auth[5u8] == 55u64);
    assert(auth[6u8] == 66u64);

    // Persist and duplicate the submap
    let mut psub1 = sub.persist();
    assert(psub1[2u8] == 22u64);
    let psub2 = psub1.duplicate();
    assert(psub2[2u8] == 22u64);

    // Not shown in this simple example is the main use case of this resource:
    // maintaining an invariant between GhostMapAuth<K, V> and some exec-mode
    // shared state with a map view (e.g., HashMap<K, V>), which states that
    // the Map<K, V> view of GhostMapAuth<K, V> is the same as the view of the
    // HashMap<K, V>, and then handing out a GhostSubmap<K, V> to different
    // clients that might need to operate on different keys in this map.
}
```

</div>

</div>

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.GhostMapAuth.html" class="struct"
title="struct vstd::tokens::map::GhostMapAuth">GhostMapAuth</a>  
A resource that has the authoritative ownership on the entire map

<a href="struct.GhostPersistentPointsTo.html" class="struct"
title="struct vstd::tokens::map::GhostPersistentPointsTo">GhostPersistentPointsTo</a>  
A resource representing duplicable client knowledge of a single key in
the map.

<a href="struct.GhostPersistentSubmap.html" class="struct"
title="struct vstd::tokens::map::GhostPersistentSubmap">GhostPersistentSubmap</a>  
A resource representing duplicable client knowledge of a persistent
submap.

<a href="struct.GhostPointsTo.html" class="struct"
title="struct vstd::tokens::map::GhostPointsTo">GhostPointsTo</a>  
A resource that asserts client ownership over a single key in the map.

<a href="struct.GhostSubmap.html" class="struct"
title="struct vstd::tokens::map::GhostSubmap">GhostSubmap</a>  
A resource that asserts client ownership of a submap.

</div>

</div>
