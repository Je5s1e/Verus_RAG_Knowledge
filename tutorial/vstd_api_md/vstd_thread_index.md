<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)

</div>

# Module thread Copy item path

<span class="sub-heading"><a href="../../src/vstd/thread.rs.html#1-273" class="src">Source</a>
</span>

</div>

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.IsThread.html" class="struct"
title="struct vstd::thread::IsThread">IsThread</a>  
<a href="struct.JoinHandle.html" class="struct"
title="struct vstd::thread::JoinHandle">JoinHandle</a>  
Object returned by [`spawn()`](fn.spawn.html "fn vstd::thread::spawn")
to allow thread joining. (Wrapper around
[`std::thread::JoinHandle`](https://doc.rust-lang.org/std/thread/struct.JoinHandle.html).)

<a href="struct.ThreadId.html" class="struct"
title="struct vstd::thread::ThreadId">ThreadId</a>  
Wrapper around Rust’s
[`ThreadId`](https://doc.rust-lang.org/std/thread/struct.ThreadId.html)
object. This is an opaque type.

## Functions<a href="#functions" class="anchor">§</a>

<a href="fn.spawn.html" class="fn"
title="fn vstd::thread::spawn">spawn</a>  
Spawns a thread. (Wrapper around
[`std::thread::spawn`](https://doc.rust-lang.org/std/thread/fn.spawn.html).)

<a href="fn.thread_id.html" class="fn"
title="fn vstd::thread::thread_id">thread_id</a>  
Gets the current thread ID using Rust’s
[`Thread::id()`](https://doc.rust-lang.org/std/thread/struct.Thread.html#method.id)
under the hood. Also returns a ghost object representing proof of being
on this thread.

</div>

</div>
