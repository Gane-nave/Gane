#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Health {
    pub service: &'static str,
    pub ready: bool,
}

pub fn readiness() -> Health {
    Health {
        service: "aurora-nav-core",
        ready: true,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn readiness_is_true() {
        let health = readiness();
        assert_eq!(health.service, "aurora-nav-core");
        assert!(health.ready);
    }
}
