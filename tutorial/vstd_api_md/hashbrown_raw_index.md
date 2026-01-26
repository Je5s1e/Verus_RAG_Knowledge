<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[hashbrown](../index.html)

</div>

# Module raw Copy item path

<span class="sub-heading"><a href="../../src/hashbrown/lib.rs.html#58" class="src">Source</a>
</span>

</div>

Expand description

<div class="docblock">

Experimental and unsafe `RawTable` API. This module is only available if
the `raw` feature is enabled.

</div>

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.Bucket.html" class="struct"
title="struct hashbrown::raw::Bucket">Bucket</a>  
A reference to a hash table bucket containing a `T`.

<a href="struct.RawDrain.html" class="struct"
title="struct hashbrown::raw::RawDrain">RawDrain</a>  
Iterator which consumes elements without freeing the table storage.

<a href="struct.RawIntoIter.html" class="struct"
title="struct hashbrown::raw::RawIntoIter">RawIntoIter</a>  
Iterator which consumes a table and returns elements.

<a href="struct.RawIter.html" class="struct"
title="struct hashbrown::raw::RawIter">RawIter</a>  
Iterator which returns a raw pointer to every full bucket in the table.

<a href="struct.RawIterHash.html" class="struct"
title="struct hashbrown::raw::RawIterHash">RawIterHash</a>  
Iterator over occupied buckets that could match a given hash.

<a href="struct.RawTable.html" class="struct"
title="struct hashbrown::raw::RawTable">RawTable</a>  
A raw hash table with an unsafe API.

</div>

</div>
