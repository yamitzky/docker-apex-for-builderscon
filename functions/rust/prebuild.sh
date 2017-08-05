docker run --rm -v "$PWD:/data" -w /data frolvlad/alpine-rust rustc -C target-feature=+crt-static ./hello.rs
