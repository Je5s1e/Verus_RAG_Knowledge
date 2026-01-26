<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[hashbrown](../index.html)

</div>

# Module hash_map Copy item path

<span class="sub-heading"><a href="../../src/hashbrown/lib.rs.html#85" class="src">Source</a>
</span>

</div>

Expand description

<div class="docblock">

A hash map implemented with quadratic probing and SIMD lookup.

</div>

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.Drain.html" class="struct"
title="struct hashbrown::hash_map::Drain">Drain</a>  
A draining iterator over the entries of a `HashMap` in arbitrary order.
The iterator element type is `(K, V)`.

<a href="struct.DrainFilter.html" class="struct"
title="struct hashbrown::hash_map::DrainFilter">DrainFilter</a>  
A draining iterator over entries of a `HashMap` which don’t satisfy the
predicate `f(&k, &mut v)` in arbitrary order. The iterator element type
is `(K, V)`.

<a href="struct.HashMap.html" class="struct"
title="struct hashbrown::hash_map::HashMap">HashMap</a>  
A hash map implemented with quadratic probing and SIMD lookup.

<a href="struct.IntoIter.html" class="struct"
title="struct hashbrown::hash_map::IntoIter">IntoIter</a>  
An owning iterator over the entries of a `HashMap` in arbitrary order.
The iterator element type is `(K, V)`.

<a href="struct.IntoKeys.html" class="struct"
title="struct hashbrown::hash_map::IntoKeys">IntoKeys</a>  
An owning iterator over the keys of a `HashMap` in arbitrary order. The
iterator element type is `K`.

<a href="struct.IntoValues.html" class="struct"
title="struct hashbrown::hash_map::IntoValues">IntoValues</a>  
An owning iterator over the values of a `HashMap` in arbitrary order.
The iterator element type is `V`.

<a href="struct.Iter.html" class="struct"
title="struct hashbrown::hash_map::Iter">Iter</a>  
An iterator over the entries of a `HashMap` in arbitrary order. The
iterator element type is `(&'a K, &'a V)`.

<a href="struct.IterMut.html" class="struct"
title="struct hashbrown::hash_map::IterMut">IterMut</a>  
A mutable iterator over the entries of a `HashMap` in arbitrary order.
The iterator element type is `(&'a K, &'a mut V)`.

<a href="struct.Keys.html" class="struct"
title="struct hashbrown::hash_map::Keys">Keys</a>  
An iterator over the keys of a `HashMap` in arbitrary order. The
iterator element type is `&'a K`.

<a href="struct.OccupiedEntry.html" class="struct"
title="struct hashbrown::hash_map::OccupiedEntry">OccupiedEntry</a>  
A view into an occupied entry in a `HashMap`. It is part of the
[`Entry`](enum.Entry.html) enum.

<a href="struct.OccupiedEntryRef.html" class="struct"
title="struct hashbrown::hash_map::OccupiedEntryRef">OccupiedEntryRef</a>  
A view into an occupied entry in a `HashMap`. It is part of the
[`EntryRef`](enum.EntryRef.html) enum.

<a href="struct.OccupiedError.html" class="struct"
title="struct hashbrown::hash_map::OccupiedError">OccupiedError</a>  
The error returned by
[`try_insert`](../struct.HashMap.html#method.try_insert "method hashbrown::HashMap::try_insert")
when the key already exists.

<a href="struct.RawEntryBuilder.html" class="struct"
title="struct hashbrown::hash_map::RawEntryBuilder">RawEntryBuilder</a>  
A builder for computing where in a
[`HashMap`](../struct.HashMap.html "struct hashbrown::HashMap") a
key-value pair would be stored.

<a href="struct.RawEntryBuilderMut.html" class="struct"
title="struct hashbrown::hash_map::RawEntryBuilderMut">RawEntryBuilderMut</a>  
A builder for computing where in a
[`HashMap`](../struct.HashMap.html "struct hashbrown::HashMap") a
key-value pair would be stored.

<a href="struct.RawOccupiedEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawOccupiedEntryMut">RawOccupiedEntryMut</a>  
A view into an occupied entry in a `HashMap`. It is part of the
[`RawEntryMut`](enum.RawEntryMut.html) enum.

<a href="struct.RawVacantEntryMut.html" class="struct"
title="struct hashbrown::hash_map::RawVacantEntryMut">RawVacantEntryMut</a>  
A view into a vacant entry in a `HashMap`. It is part of the
[`RawEntryMut`](enum.RawEntryMut.html) enum.

<a href="struct.VacantEntry.html" class="struct"
title="struct hashbrown::hash_map::VacantEntry">VacantEntry</a>  
A view into a vacant entry in a `HashMap`. It is part of the
[`Entry`](enum.Entry.html) enum.

<a href="struct.VacantEntryRef.html" class="struct"
title="struct hashbrown::hash_map::VacantEntryRef">VacantEntryRef</a>  
A view into a vacant entry in a `HashMap`. It is part of the
[`EntryRef`](enum.EntryRef.html) enum.

<a href="struct.Values.html" class="struct"
title="struct hashbrown::hash_map::Values">Values</a>  
An iterator over the values of a `HashMap` in arbitrary order. The
iterator element type is `&'a V`.

<a href="struct.ValuesMut.html" class="struct"
title="struct hashbrown::hash_map::ValuesMut">ValuesMut</a>  
A mutable iterator over the values of a `HashMap` in arbitrary order.
The iterator element type is `&'a mut V`.

## Enums<a href="#enums" class="anchor">§</a>

<a href="enum.DefaultHashBuilder.html" class="enum"
title="enum hashbrown::hash_map::DefaultHashBuilder">DefaultHashBuilder</a>  
Dummy default hasher for `HashMap`.

<a href="enum.Entry.html" class="enum"
title="enum hashbrown::hash_map::Entry">Entry</a>  
A view into a single entry in a map, which may either be vacant or
occupied.

<a href="enum.EntryRef.html" class="enum"
title="enum hashbrown::hash_map::EntryRef">EntryRef</a>  
A view into a single entry in a map, which may either be vacant or
occupied, with any borrowed form of the map’s key type.

<a href="enum.RawEntryMut.html" class="enum"
title="enum hashbrown::hash_map::RawEntryMut">RawEntryMut</a>  
A view into a single entry in a map, which may either be vacant or
occupied.

</div>

</div>
