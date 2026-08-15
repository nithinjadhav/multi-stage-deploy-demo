import unittest

from scripts.promotion import PromotionStage, validate_stage, stage_order


class PromotionTests(unittest.TestCase):
    def test_stage_order_is_fixed(self):
        self.assertEqual(stage_order(), ["dev", "qa", "stg", "prd"])

    def test_valid_stage_accepts_known_names(self):
        for stage in ["dev", "qa", "stg", "prd"]:
            self.assertEqual(validate_stage(stage), stage)

    def test_invalid_stage_rejected(self):
        with self.assertRaises(ValueError):
            validate_stage("prod")

    def test_stage_enum_matches_expected_sequence(self):
        self.assertEqual(PromotionStage.DEV.value, "dev")
        self.assertEqual(PromotionStage.QA.value, "qa")
        self.assertEqual(PromotionStage.STG.value, "stg")
        self.assertEqual(PromotionStage.PRD.value, "prd")


if __name__ == "__main__":
    unittest.main()
