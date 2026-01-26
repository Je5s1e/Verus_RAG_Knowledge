<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)

</div>

# Module buffer Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/buffer.rs.html#1-435"
class="src">Source</a> </span>

</div>

Expand description

<div class="docblock">

A stably addressed token buffer supporting efficient traversal based on
a cheaply copyable cursor.

</div>

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.Cursor.html" class="struct"
title="struct verus_syn::buffer::Cursor">Cursor</a>  
A cheaply copyable cursor into a `TokenBuffer`.

<a href="struct.TokenBuffer.html" class="struct"
title="struct verus_syn::buffer::TokenBuffer">TokenBuffer</a>  
A buffer that can be efficiently traversed multiple times, unlike
`TokenStream` which requires a deep copy in order to traverse more than
once.

</div>

</div>
