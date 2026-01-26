<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)

</div>

# Module tokens Copy item path

<span class="sub-heading"><a href="../../src/vstd/tokens.rs.html#1-636" class="src">Source</a>
</span>

</div>

## Modules<a href="#modules" class="anchor">§</a>

<a href="frac/index.html" class="mod"
title="mod vstd::tokens::frac">frac</a>  
<a href="map/index.html" class="mod"
title="mod vstd::tokens::map">map</a>  
Maps that support ownership of keys

<a href="seq/index.html" class="mod"
title="mod vstd::tokens::seq">seq</a>  
<a href="set/index.html" class="mod"
title="mod vstd::tokens::set">set</a>  
Implementation of a resource for ownership of subsets of values in a set

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.InstanceId.html" class="struct"
title="struct vstd::tokens::InstanceId">InstanceId</a>

Unique identifier for every VerusSync instance. Every “Token” and
“Instance” object has an `InstanceId`. These ID values must agree to
perform any token operation.

<a href="struct.MapToken.html" class="struct"
title="struct vstd::tokens::MapToken">MapToken</a>

<a href="struct.MultisetToken.html" class="struct"
title="struct vstd::tokens::MultisetToken">MultisetToken</a>

<a href="struct.SetToken.html" class="struct"
title="struct vstd::tokens::SetToken">SetToken</a>

## Traits<a href="#traits" class="anchor">§</a>

<a href="trait.CountToken.html" class="trait"
title="trait vstd::tokens::CountToken">CountToken</a>  
Interface for VerusSync tokens created for a field marked with the
`count` strategy.

<a href="trait.ElementToken.html" class="trait"
title="trait vstd::tokens::ElementToken">ElementToken</a>  
Interface for VerusSync tokens created for a field marked with the
`set`, `persistent_set` or `multiset` strategies.

<a href="trait.KeyValueToken.html" class="trait"
title="trait vstd::tokens::KeyValueToken">KeyValueToken</a>  
Interface for VerusSync tokens created for a field marked with the `map`
or `persistent_map` strategies.

<a href="trait.MonotonicCountToken.html" class="trait"
title="trait vstd::tokens::MonotonicCountToken">MonotonicCountToken</a>  
Interface for VerusSync tokens created for a field marked with the
`persistent_count` strategy.

<a href="trait.SimpleToken.html" class="trait"
title="trait vstd::tokens::SimpleToken">SimpleToken</a>  
Interface for VerusSync tokens created for a field marked with the
`bool` or `persistent_bool` strategy.

<a href="trait.UniqueElementToken.html" class="trait"
title="trait vstd::tokens::UniqueElementToken">UniqueElementToken</a>  
Interface for VerusSync tokens created for a field marked with the `set`
strategy.

<a href="trait.UniqueKeyValueToken.html" class="trait"
title="trait vstd::tokens::UniqueKeyValueToken">UniqueKeyValueToken</a>  
Interface for VerusSync tokens created for a field marked with the `map`
strategy.

<a href="trait.UniqueSimpleToken.html" class="trait"
title="trait vstd::tokens::UniqueSimpleToken">UniqueSimpleToken</a>  
Interface for VerusSync tokens created for a field marked with the
`bool` strategy.

<a href="trait.UniqueValueToken.html" class="trait"
title="trait vstd::tokens::UniqueValueToken">UniqueValueToken</a>  
Interface for VerusSync tokens created for a field marked with the
`variable` or `option` strategies.

<a href="trait.ValueToken.html" class="trait"
title="trait vstd::tokens::ValueToken">ValueToken</a>  
Interface for VerusSync tokens created for a field marked with the
`variable`, `option` or `persistent_option` strategies.

</div>

</div>
