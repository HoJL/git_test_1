from abc import ABC, abstractmethod


class BenefitStrategy(ABC):
    @abstractmethod
    def apply_benefit(self, amount):
        pass

class BaseBenefit(BenefitStrategy):
    def apply_benefit(self, amount):
        benefit = amount * 0.02
        print(f'Base Benefit: {benefit}')
        return amount + benefit 