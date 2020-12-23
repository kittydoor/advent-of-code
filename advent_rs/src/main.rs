use std::fs;
use structopt::StructOpt;
use anyhow::{Context, Result};

mod y2020_day01;
mod y2020_day02;
mod y2020_day03;

#[derive(StructOpt)]
struct Cli {
    /// Challenge identifier in the format of <year>-<day>
    challenge: String,
    /// Challenge part (p1 or p2)
    part: String,
    /// Input file path
    #[structopt(parse(from_os_str))]
    path: std::path::PathBuf,
}

fn main() -> Result<()> {
    let args = Cli::from_args();

    let content = fs::read_to_string(&args.path)
        .with_context(|| format!("could not read file `{}`",
                                 args.path.to_str().unwrap()))?;

    let result = match args.challenge.as_str() {
        "2020-01" => y2020_day01::report_repair(&content, &args.part),
        "2020-02" => y2020_day02::password_philosophy(&content, &args.part),
        "2020-03" => y2020_day03::toboggan_trajectory(&content, &args.part),
        _ => panic!("Challenge {} not implemented", args.challenge),
    };

    println!("{}", result.ok().unwrap());

    Ok(())
}
