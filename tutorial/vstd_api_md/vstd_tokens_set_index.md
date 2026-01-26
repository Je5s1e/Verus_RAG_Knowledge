<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../../index.html)::[tokens](../index.html)

</div>

# Module set Copy item path

<span class="sub-heading"><a href="../../../src/vstd/tokens/set.rs.html#1-888"
class="src">Source</a> </span>

</div>

Expand description

<div class="docblock">

Implementation of a resource for ownership of subsets of values in a set

- [`GhostSetAuth<T>`](struct.GhostSetAuth.html "struct vstd::tokens::set::GhostSetAuth")
  represents authoritative ownership of the entire set;
- [`GhostSubset<T>`](struct.GhostSubset.html "struct vstd::tokens::set::GhostSubset")
  represents client ownership of some subset;
- [`GhostPersistentSubset<T>`](struct.GhostPersistentSubset.html "struct vstd::tokens::set::GhostPersistentSubset")
  represents duplicable client knowledge of some persistent subset;
- [`GhostSingleton<T>`](struct.GhostSingleton.html "struct vstd::tokens::set::GhostSingleton")
  represents client ownership of a singleton.
- [`GhostPersistentSingleton<T>`](struct.GhostPersistentSingleton.html "struct vstd::tokens::set::GhostPersistentSingleton")
  represents duplicable client knowledge of a persistent singleton;

Updating the authoritative `GhostSetAuth<T>` requires a `GhostSubset<T>`
containing the values being updated.

`GhostSubset<T>`s can be combined or split. Whenever a `GhostSubset<T>`
can be used, we can instead use a `GhostSingleton<T>` (but not
vice-versa).

`GhostPersistentSubset<T>`s can be combined or split. Whenever a
`GhostPersistentSubset<T>` can be used, we can instead use a
`GhostPersistentSingleton<T>` (but not vice-versa).

#### <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
fn example_use() {
    let tracked (mut auth, mut sub) = GhostSetAuth::new(set![1u8, 2u8, 3u8]);

    // Allocate some more values in the auth set, receiving a new subset.
    let tracked sub2 = auth.insert_set(set![4u8, 5u8]);
    proof { sub.combine(sub2); }

    // Allocate a single value in the auth set, receiving a points to
    let tracked pt1 = auth.insert(6u8);
    proof { sub.combine_points_to(pt1); }

    // Delete some values in the auth set, by returning corresponding subset.
    let tracked sub3 = sub.split(set![3u8, 4u8]);
    proof { auth.delete(sub3); }

    // Split the subset into a singleton and a subset
    let tracked pt1 = sub.split_singleton(1u8);
    let tracked sub4 = sub.split(set![5u8, 6u8]);

    // In general, we might need to call agree() to establish the fact that
    // a singleton/subset has the same values as the auth set.  Here, Verus
    // doesn't need agree because it can track where both the auth, singleton
    // and subset came from.
    proof { sub.agree(&auth); }
    proof { pt1.agree(&auth); }
    proof { sub4.agree(&auth); }

    assert(auth@.contains(pt1@));
    assert(sub4@ <= auth@);
    assert(sub@ <= auth@);

    // Persist and duplicate the submap
    let mut psub1 = sub.persist();
    assert(psub1.contains(2u8));
    let psub2 = psub1.duplicate();
    assert(psub2.contains(2u8));

    // Not shown in this simple example is the main use case of this resource:
    // maintaining an invariant between GhostSetAuth<T> and some exec-mode
    // shared state with a map view (e.g., HashSet<T>), which states that
    // the Set<T> view of GhostSetAuth<T> is the same as the view of the
    // HashSet<T>, and then handing out a GhostSubset<T> to different
    // clients that might need to operate on different values in the set
}
```

</div>

</div>

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.GhostPersistentSingleton.html" class="struct"
title="struct vstd::tokens::set::GhostPersistentSingleton">GhostPersistentSingleton</a>  
A resource that asserts duplicable client knowledge of a persistent
singleton

<a href="struct.GhostPersistentSubset.html" class="struct"
title="struct vstd::tokens::set::GhostPersistentSubset">GhostPersistentSubset</a>  
A resource that asserts duplicable client knowledge of a persistent
subset

<a href="struct.GhostSetAuth.html" class="struct"
title="struct vstd::tokens::set::GhostSetAuth">GhostSetAuth</a>  
A resource that has the authoritative ownership on the entire set

<a href="struct.GhostSingleton.html" class="struct"
title="struct vstd::tokens::set::GhostSingleton">GhostSingleton</a>  
A resource that has client ownership of a singleton

<a href="struct.GhostSubset.html" class="struct"
title="struct vstd::tokens::set::GhostSubset">GhostSubset</a>  
A resource that has client ownership of a subset

</div>

</div>
