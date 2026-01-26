<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)

</div>

# Module storage_protocol Copy item path

<span class="sub-heading"><a href="../../src/vstd/storage_protocol.rs.html#1-343"
class="src">Source</a> </span>

</div>

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.StorageResource.html" class="struct"
title="struct vstd::storage_protocol::StorageResource">StorageResource</a>  
Interface for “storage protocol” ghost state. This is an
extension-slash-variant on the more well-known concept of “PCM” ghost
state, which we also have an interface for
[here](../pcm/struct.Resource.html "struct vstd::pcm::Resource"). The
unique feature of a storage protocol is the ability to use
[`guard`](StorageResource::guard) to manipulate *shared* references of
ghost state.

## Traits<a href="#traits" class="anchor">§</a>

<a href="trait.Protocol.html" class="trait"
title="trait vstd::storage_protocol::Protocol">Protocol</a>  
See
[`StorageResource`](struct.StorageResource.html "struct vstd::storage_protocol::StorageResource")
for more information.

</div>

</div>
