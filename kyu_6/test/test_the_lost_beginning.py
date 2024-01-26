import kyu_6.src.the_lost_beginning as solution
import codewars_test as test

@test.describe("Tests")
def tests():
    # Use "it" to identify the conditions you are testing for
    @test.it("Basic")
    def test_find():
        test.assert_equals(solution.find("123456789101112131415"), 1)
        test.assert_equals(solution.find("17181920"), 17)
        test.assert_equals(solution.find("72637236"), 72637236)
        test.assert_equals(solution.find("1112"), 11)
        test.assert_equals(solution.find("91011"), 9)
        test.assert_equals(solution.find("99100"), 99)
        test.assert_equals(solution.find("431243"), 431243)
        test.assert_equals(solution.find("577495"), 577495)
        test.assert_equals(solution.find("1234567891"), 1234567891)