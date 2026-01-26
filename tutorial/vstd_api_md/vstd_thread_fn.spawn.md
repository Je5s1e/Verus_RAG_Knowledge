<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[thread](index.html)

</div>

# Function <span class="fn">spawn</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/thread.rs.html#107-133" class="src">Source</a>
</span>

</div>

``` rust
pub fn spawn<F, Ret>(f: F) -> JoinHandle<Ret>where
    F: FnOnce() -> Ret + Send + 'static,
    Ret: Send + 'static,
```

Expand description

<div class="docblock">

Spawns a thread. (Wrapper around
[`std::thread::spawn`](https://doc.rust-lang.org/std/thread/fn.spawn.html).)

This takes as input a `FnOnce` closure with no arguments. The `spawn`
returns a
[`JoinHandle`](struct.JoinHandle.html "struct vstd::thread::JoinHandle"),
on which the client can call
[`join()`](struct.JoinHandle.html#method.join "method vstd::thread::JoinHandle::join")
to wait for the thread to complete. The return value of the closure is
returned via `join()`.

The closure must be callable (i.e., its precondition must be satisfied)
but it may have an arbitrary postcondition. The postcondition is passed
through the `JoinHandle` via
[`JoinHandle::predicate()`](JoinHandle::predicate).

#### <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap ignore">

<a href="#" class="tooltip" title="This example is not tested">ⓘ</a>

``` rust
struct MyInteger {
    u: u64,
}

fn main() {
    // Construct an object to pass into the thread.
    let my_int = MyInteger { u: 5 };

    // Spawn a new thread.
    let join_handle = spawn(move || {
        ensures(|return_value: MyInteger|
            return_value.u == 20);

        // Move the `my_int` object into the closure.
        let mut my_int_on_another_thread = my_int;

        // Update its value.
        my_int_on_another_thread.u = 20;

        // Return it.
        my_int_on_another_thread
    });

    // Wait for the thread to finish its work.
    let result_my_int = join_handle.join();

    match result_my_int {
        Result::Ok(my_int) => {
            // Obtain the `MyInteger` object that was passed
            // back from the spawned thread.
            // Assert that it has the right value.
            assert(my_int.u == 20);
        }
        Result::Err(_) => { }
    }
}
```

</div>

</div>

</div>

</div>
