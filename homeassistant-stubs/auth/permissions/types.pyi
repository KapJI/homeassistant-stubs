from collections.abc import Mapping

ValueType = Mapping[str, bool] | bool | None
SubCategoryDict = Mapping[str, ValueType]
SubCategoryType = SubCategoryDict | bool | None
CategoryType = Mapping[str, SubCategoryType] | Mapping[str, ValueType] | bool | None
PolicyType = Mapping[str, CategoryType]
