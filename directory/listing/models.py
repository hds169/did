from __future__ import unicode_literals

from django.db import models


from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

    
class article(models.Model):
    name=models.CharField(max_length=100)
    domain=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=100)
    def __str__(self):
        return self.domain
 
class linkimp(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class linkmid(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class link(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    def __str__(self):
        return self.name


#models under arts and humanities
class art_history1(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class art_weblog2(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class artist3(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class awards4(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class booksell5(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class censor6(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class chats7(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class crafts8(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class critic9 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class culture10(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class culturepolicy11(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class design12(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class education13(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class events14(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class humanities15(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class institutes16(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class jobs17(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class museums18(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class news19(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class organizations20(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class performing21(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class refernce22(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class shopping23(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class visual24(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class localhistory25(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class photography26(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

#Models under Buisness & Economy

class buisness_resources27(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class buisness_libraries28(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class buisness_schools29(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class chats30(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class classified31(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class cooperative32(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class directories_of_services33(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class economics34(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class buisness_training35(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class employment_work36(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class ethics_responsibity37(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class finance_investment38(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class global_economy39(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class history40(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class intellectual_property41(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class labor42(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class law43(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class marketing_advertising44(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class news_media45(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class organization46(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class taxes47(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class trade48(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class transportation49(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class publishing_industries50(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class realestate_property51(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class work_home52(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class opportunities53(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class consultancy54(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class security55(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class services56(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class affiliate_schemes57(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class building_factories58(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class id_cards59(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class retail_equipment60(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class industrial_equipment61(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class trade_shows62(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class charity63(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

#models under computer & internet

class communications_networking64(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class computer_generations65(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class computer_science66(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class computer_technology67(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class contests68(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class conventions_trade69(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class countries70(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class cyberculture71(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class data_formats72(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class desktop_customization73(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class desktop_publishing74(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class dictionaries75(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class employment76(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class ethics77(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class forensics78(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class games79(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class graphics80(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class hardware81(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class history82(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class humor83(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class industry_information84(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class information_technology85(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class internet86(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class issues87(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class macintosh88(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class magazines89(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class mobile_computing90(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class multimedia91(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class news_media92(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class operating_systems93(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class organizations94(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class people95(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class product_info96(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class pda97(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class programming_development98(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class security_encryption99(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class software100(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class standard101(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class supercomputing102(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class technical_guides103(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class telecommunications104(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class training105(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class web_directories106(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class user_groups107(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class virtual_reality108(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class world_wide109(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class ebooks110(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class webmaster111(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class design_development112(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class domain_name113(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class seo114(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class isp115(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class tools_resources116(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class web_hosting117(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class templates118(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class image_hosting119(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class file_hosting120(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class article_directories121(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class script_services122(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class anti_virus123(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class anti_spyware124(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class url_services125(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class printers126(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class podcasts127(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title
#Models under education.
class academic_competitions128(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class biblographies129(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class languages130(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class buisness_buisness131(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class career_vocational132(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class chat133(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class confrences134(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class correctional135(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class disabilities136(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class early_childhood137(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class education138(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class equity139(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class financial_aid140(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class goverment_agencies141(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class graduation142(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class history143(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class instructional_technology144(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class job_employment145(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class journal146(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class legislations147(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class literacy148(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class news_media149(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class organizations150(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class policy151(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class programs152(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class reform153(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class shopping_services154(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class special_education155(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class standard_testing156(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class statistics157(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class teaching158(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class theory_methods159(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class online_courses160(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class driving_schools161(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title
#models under entertainment
class amusement_parks162(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class awards163(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class books_literature164(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class chat165(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class comedy166(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class tv167(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class contests168(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class ecards169(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class employment170(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class entertainment171(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class events172(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class fan_listing173(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class food_drinks174(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class movies175(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class games176(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class genres177(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class history178(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class magic179(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class news180(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class organization181(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class performing_arts182(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class radio183(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class randomized_things184(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class reviews185(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class shopping_services186(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class sports_entertainment187(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class trivia188(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class villains189(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class podcasts190(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class webisodes191(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class weblogs192(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class x_of_day193(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

#Model under health

class alternative_medicine194(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class chat195(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class children_health196(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class conferences197(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class consumer_products198(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class dental_health199(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class disabilites200(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class diseases201(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class education202(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class emergency_services203(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class enviormental_health204(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class first_aid205(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class fitness206(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class general_health207(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class health_administration208(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class health_medicine209(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class health_care210(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class hospitals211(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class hygiene212(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class institutes213(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class job_employment214(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class long_term215(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class medical_geography216(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class medicine217(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class men_health218(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class mental_health219(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class midwifery220(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class news_media221(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class nursing222(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class nutrition223(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class organizations224(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class pet_health225(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class pharmacy226(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class procedures_therapies227(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class professional_supplies228(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class public_health229(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class refernce230(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class reproductive_health231(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class senior_health232(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class sexual_health233(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class teen_health234(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class traditional_medicine235(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class travel_health236(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class societies237(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class weight_issues238(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class women_health239(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class workplace240(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class spas241(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

#Models under news & Media

class arts_humanities242(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title



class automotive243(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class buisness244(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class college_university245(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class computers_internet246(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class crime247(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class cultures248(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class education249(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class disabilities250(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class entertainment251(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class enviorment252(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class good_news253(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class government254(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class health255(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class history256(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class home_garden257(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class humor258(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class law259(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class literature260(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class news_kids261(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class outdoors262(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class philanthrophy263(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class politics264(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class real_estate265(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class religion266(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class science267(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class sports268(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class technology269(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class traffic_road270(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class transportation271 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class travel_update272(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class weather273(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class weird_news274(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

#Models under Recreation & Sports

class amusement_theme275(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class automotive276(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class aviation277 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class bookseller278(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class chat279(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class cooking280(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class dance281(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class events282(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class fitness283(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class gambling284(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class hobbies285(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class job_employment286(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class magazines287(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class motorcycles288(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class outdoors289(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class sports290(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class television291(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class toys292(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class theatre293(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class fishing294 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class sailing295(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class dating296(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class board_games297(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class travel298(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class acronyms_abbreavations299(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class general300(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class alamanacs301(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class geographic_name302(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class arts_humanities303(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class health304(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class ask_expert305(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class journals306(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class bibliographies307(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class maps308(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class biographies309(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class measurments310(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class book_sellers311(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class music312(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class codes313(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class country_profiles314(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class directories315(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class english_language316(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class enviorment317(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class etiquette318(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class faq319(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class finance_investments320(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class flags321(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class parliamentary_procedure322(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class patents323(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class research_papers324(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class science325(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class searching_web326(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class standards327(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class statistics328(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class student_resources329(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class time330(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class quotes331 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title



class weather332 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


#Models UNder Science and Technology

class aeronautics_aerospace333(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class agriculture334 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class animals_insect335(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class anthropology_archeaology336(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class artifical_life337(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class astronomy338 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class biology339(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class chemistry340 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class cognitive_science341(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class complex_systems342(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class computer_science343(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class earth_science344(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class ecology345(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class energy346 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class engineering347(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class forensics348(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class geography349 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class geology_geophysics350(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class hydrology351(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class information_technology352(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class life_sciences353(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class mathematics354 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class medicine355(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class meteorology356(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class nanotechnology357(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class physics358(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class psychology359(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class space360(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class science_technology361(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class chats362(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class alternative_energy363(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

#Models under Shopping

class antiques_collectibles364(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class automotive365(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class home_garden366(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class jewelry367(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class beauty_products368 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class major_retailers369(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class books370(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class music371(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class children372(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class clothing373(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class office_products374(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class computers375 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class pets376 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class consumer_electronics377(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class publications378(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class crafts379(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class sports380(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class entertainment381 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class flowers382 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class tools383 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class toys_games384(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class computer_games385(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class gifts386(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class vehicle_hire387(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class visual_arts388(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class health389(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class wedding390(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class seasonal391(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class wholesale392(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class chemicals393(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class electronics_electrical394(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class auctions395 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class comparison_services396(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class food_drink397(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class shopping_service398 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

#Models under Blogs

class buisness401(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class education402 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class library403(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class politics404(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class science405(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class eclectic406(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class law407(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class personal408 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class technology409 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class computer410(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class internet411(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class news412(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class money413 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class webmaster414 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class blog_hosting415(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class music416 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class making_money417 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class home_garden418 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

#Modeles under society

class activism419 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class advice420 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class crime421(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class death422(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class disabled423 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class economics424(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class ethnicity425(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class history426 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class folklore427 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class future428 (models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class geology429(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class language_linguistics430(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class military431(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class organizations432(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class people433(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class religion_spirituality434(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class social_sciences435(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class subcultures436(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class support_groups437(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class urban_legends438(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title


class work439(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class men440(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class women441(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    mkeyword=models.CharField(max_length=100)
    mdescription=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reciprocal=models.CharField(max_length=100)
    def __str__(self):
        return self.title

