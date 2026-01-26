<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../../index.html)::[tokens](../index.html)

</div>

# Module frac Copy item path

<span class="sub-heading"><a href="../../../src/vstd/tokens/frac.rs.html#1-733"
class="src">Source</a> </span>

</div>

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.Empty.html" class="struct"
title="struct vstd::tokens::frac::Empty">Empty</a>  
Token that represents the “empty” state of a fractional resource system.
See [`Frac`](struct.Frac.html "struct vstd::tokens::frac::Frac") for
more information.

<a href="struct.Frac.html" class="struct"
title="struct vstd::tokens::frac::Frac">Frac</a>  
Token that maintains fractional access to some resource. This allows
multiple clients to obtain shared references to some resource via
`borrow`.

<a href="struct.FracGhost.html" class="struct"
title="struct vstd::tokens::frac::FracGhost">FracGhost</a>  
An implementation of a resource for fractional ownership of a ghost
variable.

<a href="struct.GhostVar.html" class="struct"
title="struct vstd::tokens::frac::GhostVar">GhostVar</a>  
See
[`GhostVarAuth<T>`](struct.GhostVarAuth.html "struct vstd::tokens::frac::GhostVarAuth")
for more information.

<a href="struct.GhostVarAuth.html" class="struct"
title="struct vstd::tokens::frac::GhostVarAuth">GhostVarAuth</a>  
`GhostVarAuth<T>` is one half of a pair of tokens—the other being
[`GhostVar<T>`](struct.GhostVar.html "struct vstd::tokens::frac::GhostVar").
These tokens each track a value, and they can only be allocated or
updated together. Thus, the pair of tokens always agree on the value,
but they can be owned separately.

</div>

</div>
