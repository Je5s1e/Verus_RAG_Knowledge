<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[proc_macro2](../index.html)::[extra](index.html)

</div>

# Function <span class="fn">invalidate_current_thread_spans</span> Copy item path

<span class="sub-heading"><a href="../../src/proc_macro2/extra.rs.html#73-75"
class="src">Source</a> </span>

</div>

``` rust
pub fn invalidate_current_thread_spans()
```

Expand description

<div class="docblock">

Invalidate any `proc_macro2::Span` that exist on the current thread.

The implementation of `Span` uses thread-local data structures and this
function clears them. Calling any method on a `Span` on the current
thread created prior to the invalidation will return incorrect values or
crash.

This function is useful for programs that process more than
2<sup>32</sup> bytes of Rust source code on the same thread. Just like
rustc, proc-macro2 uses 32-bit source locations, and these wrap around
when the total source code processed by the same thread exceeds
2<sup>32</sup> bytes (4 gigabytes). After a wraparound, `Span` methods
such as `source_text()` can return wrong data.

## <a href="#example" class="doc-anchor">§</a>Example

As of late 2023, there is 200 GB of Rust code published on crates.io.
Looking at just the newest version of every crate, it is 16 GB of code.
So a workload that involves parsing it all would overflow a 32-bit
source location unless spans are being invalidated.

<div class="example-wrap">

``` rust
use flate2::read::GzDecoder;
use std::ffi::OsStr;
use std::io::{BufReader, Read};
use std::str::FromStr;
use tar::Archive;

rayon::scope(|s| {
    for krate in every_version_of_every_crate() {
        s.spawn(move |_| {
            proc_macro2::extra::invalidate_current_thread_spans();

            let reader = BufReader::new(krate);
            let tar = GzDecoder::new(reader);
            let mut archive = Archive::new(tar);
            for entry in archive.entries().unwrap() {
                let mut entry = entry.unwrap();
                let path = entry.path().unwrap();
                if path.extension() != Some(OsStr::new("rs")) {
                    continue;
                }
                let mut content = String::new();
                entry.read_to_string(&mut content).unwrap();
                match proc_macro2::TokenStream::from_str(&content) {
                    Ok(tokens) => {/* ... */},
                    Err(_) => continue,
                }
            }
        });
    }
});
```

</div>

## <a href="#panics" class="doc-anchor">§</a>Panics

This function is not applicable to and will panic if called from a
procedural macro.

</div>

</div>

</div>
