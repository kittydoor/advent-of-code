use itertools::Itertools;

pub fn report_repair(contents: &str, part: &str) -> Result<String, String> {
    let expenses: Vec<u32> = contents
        .lines()
        .map(|x| u32::from_str_radix(x, 10))
        .map(|x| x.unwrap())
        .collect();

    match part {
        "p1" => Ok(report_repair_p1(&expenses).to_string()),
        "p2" => Ok(report_repair_p2(&expenses).to_string()),
        _ => Err("<part> must be p1 or p2!".to_string()),
    }
}

fn report_repair_p1(expenses: &[u32]) -> u32  {
    let filtered: Vec<_> = expenses
        .iter()
        .filter_map(|expense| {
            let other: Vec<_> = expenses
                .iter()
                .filter(|&&o| o == 2020 - expense)
                .collect();

            if other.is_empty() {
                None
            } else {
                Some((expense, other[0]))
            }
        })
        .collect();

    let pair = filtered
        .first()
        .unwrap();

    pair.0 * pair.1
}

fn report_repair_p2(expenses: &[u32]) -> u32  {
    let filtered: Vec<_> = expenses
        .iter()
        .combinations(3)
        .filter(|triple| {
            println!("{:?}", triple);
            triple.into_iter().fold(0, |x, &y| x + y) == 2020
        })
        .collect();

    let triple = filtered
        .first()
        .unwrap();

    triple.iter().fold(1, |x, &y| x * y)
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE_DATA: [u32; 6] = [1721, 979, 366, 299, 675, 1456];

    #[test]
    fn example_p1() {
        assert_eq!(1721 * 299, report_repair_p1(&EXAMPLE_DATA));
    }

    #[test]
    fn example_p2() {
        assert_eq!(979 * 366 * 675, report_repair_p2(&EXAMPLE_DATA));
    }
}
