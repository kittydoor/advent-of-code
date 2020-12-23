use regex::Regex;

pub fn password_philosophy(contents: &str, part: &str) -> Result<String, String> {
    let passwords: Vec<&str> = contents
        .lines()
        .map(|line| line.trim())
        .collect();

    match part {
        "p1" => Ok(password_philosophy_p1(&passwords).to_string()),
        "p2" => Ok(password_philosophy_p2(&passwords).to_string()),
        _ => Err("<part> must be p1 or p2!".to_string()),
    }
}

#[derive(Debug)]
struct Entry {
    min: u32,
    max: u32,
    ch: char,
    phrase: String,
}

fn password_philosophy_p1(passwords: &[&str]) ->  u32 {
    let re = Regex::new(
        r"^(?P<min>\d+)-(?P<max>\d+) (?P<ch>[a-z]): (?P<phrase>[a-z]+)$"
        ).unwrap();

    let check = |entry: &Entry| {
        let count = entry.phrase
            .chars()
            .filter(|&c| c == entry.ch)
            .collect::<Vec<_>>()
            .len() as u32;

        entry.min <= count && count <= entry.max
    };

    passwords
        .iter()
        .map(|line| {
            let caps = re
                .captures(line)
                .unwrap();

            Entry {
                min: caps.name("min").unwrap().as_str().parse().unwrap(),
                max: caps.name("max").unwrap().as_str().parse().unwrap(),
                ch: caps.name("ch").unwrap().as_str().chars().next().unwrap(),
                phrase: caps.name("phrase").unwrap().as_str().to_string(),
            }
        })
        .filter(|entry| check(entry))
        .collect::<Vec<_>>()
        .len() as u32
}

fn password_philosophy_p2(passwords: &[&str]) ->  u32 {
    let re = Regex::new(
        r"^(?P<min>\d+)-(?P<max>\d+) (?P<ch>[a-z]): (?P<phrase>[a-z]+)$"
        ).unwrap();

    let check = |entry: &Entry| {
        let left = entry.phrase
            .chars()
            .nth(entry.min as usize - 1)
            .unwrap() == entry.ch;

        let right = entry.phrase
            .chars()
            .nth(entry.max as usize - 1)
            .unwrap() == entry.ch;

        left != right
    };

    passwords
        .iter()
        .map(|line| {
            let caps = re
                .captures(line)
                .unwrap();

            Entry {
                min: caps.name("min").unwrap().as_str().parse().unwrap(),
                max: caps.name("max").unwrap().as_str().parse().unwrap(),
                ch: caps.name("ch").unwrap().as_str().chars().next().unwrap(),
                phrase: caps.name("phrase").unwrap().as_str().to_string(),
            }
        })
        .filter(|entry| check(entry))
        .collect::<Vec<_>>()
        .len() as u32
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE_DATA: [&str; 3] = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    ];

    #[test]
    fn example_p1() {
        assert_eq!(2, password_philosophy_p1(&EXAMPLE_DATA));
    }

    #[test]
    fn example_p2() {
        assert_eq!(1, password_philosophy_p2(&EXAMPLE_DATA));
    }

    #[test]
    fn p2_both_contain() {
        const DATA: [&str; 2] = [
            "1-3 a: abade",
            "2-4 b: abcbe",
        ];
        assert_eq!(0, password_philosophy_p2(&DATA));
    }

    #[test]
    fn p2_one_contains() {
        const DATA: [&str; 2] = [
            "1-3 a: abcde",
            "2-4 b: abcde",
        ];
        assert_eq!(2, password_philosophy_p2(&DATA));
    }

    #[test]
    fn p2_neither_contain() {
        const DATA: [&str; 2] = [
            "1-3 b: abcde",
            "2-4 a: abcde",
        ];
        assert_eq!(0, password_philosophy_p2(&DATA));
    }
}
