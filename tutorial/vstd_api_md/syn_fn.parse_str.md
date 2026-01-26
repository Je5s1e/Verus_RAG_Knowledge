<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](index.html)

</div>

# Function <span class="fn">parse_str</span> Copy item path

<span class="sub-heading"><a href="../src/syn/lib.rs.html#956-958" class="src">Source</a>
</span>

</div>

``` rust
pub fn parse_str<T: Parse>(s: &str) -> Result<T>
```

Expand description

<div class="docblock">

Parse a string of Rust code into the chosen syntax tree node.

This function enforces that the input is fully parsed. If there are any
unparsed tokens at the end of the stream, an error is returned.

## <a href="#hygiene" class="doc-anchor">§</a>Hygiene

Every span in the resulting syntax tree will be set to resolve at the
macro call site.

## <a href="#examples" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use syn::{Expr, Result};

fn run() -> Result<()> {
    let code = "assert_eq!(u8::max_value(), 255)";
    let expr = syn::parse_str::<Expr>(code)?;
    println!("{:#?}", expr);
    Ok(())
}
```

</div>

</div>

</div>

</div>
