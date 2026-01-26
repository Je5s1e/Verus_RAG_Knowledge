<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[thread](index.html)

</div>

# Function <span class="fn">thread_id</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/thread.rs.html#200-207" class="src">Source</a>
</span>

</div>

``` rust
pub fn thread_id() -> (ThreadId, Tracked<IsThread>)
```

Expand description

<div class="docblock">

Gets the current thread ID using Rust’s
[`Thread::id()`](https://doc.rust-lang.org/std/thread/struct.Thread.html#method.id)
under the hood. Also returns a ghost object representing proof of being
on this thread.

</div>

</div>

</div>
