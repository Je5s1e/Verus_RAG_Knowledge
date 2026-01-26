<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](index.html)

</div>

# Function <span class="fn">parse_file</span> Copy item path

<span class="sub-heading"><a href="../src/verus_syn/lib.rs.html#1001-1025" class="src">Source</a>
</span>

</div>

``` rust
pub fn parse_file(content: &str) -> Result<File>
```

Expand description

<div class="docblock">

Parse the content of a file of Rust code.

This is different from `syn::parse_str::<File>(content)` in two ways:

- It discards a leading byte order mark `\u{FEFF}` if the file has one.
- It preserves the shebang line of the file, such as
  `#!/usr/bin/env rustx`.

If present, either of these would be an error using `from_str`.

## <a href="#examples" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use std::error::Error;
use std::fs;
use std::io::Read;

fn run() -> Result<(), Box<dyn Error>> {
    let content = fs::read_to_string("path/to/code.rs")?;
    let ast = syn::parse_file(&content)?;
    if let Some(shebang) = ast.shebang {
        println!("{}", shebang);
    }
    println!("{} items", ast.items.len());

    Ok(())
}
```

</div>

</div>

</div>

</div>
