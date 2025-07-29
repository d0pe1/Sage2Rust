use std::collections::HashMap;

pub type IniData = HashMap<String, HashMap<String, String>>;

pub fn parse_ini(content: &str) -> IniData {
    let mut data: IniData = HashMap::new();
    let mut current = String::new();
    for line in content.lines() {
        let line = line.trim();
        if line.starts_with('[') && line.ends_with(']') {
            current = line[1..line.len()-1].to_string();
        } else if let Some((k, v)) = line.split_once('=') {
            data.entry(current.clone()).or_default().insert(k.trim().to_string(), v.trim().to_string());
        }
    }
    data
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parse_simple_ini() {
        let input = "[Section]\nKey=Value";
        let parsed = parse_ini(input);
        assert_eq!(parsed.get("Section").unwrap().get("Key").unwrap(), "Value");
    }
}
