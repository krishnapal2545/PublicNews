-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 25, 2021 at 08:28 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `publicnews`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` int(11) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`id`, `Name`, `Email`, `Message`) VALUES
(1, 'Krishna Kumar Rajendra Prasad Pal', 'Krishnapal2545@gmail.com', 'hii');

-- --------------------------------------------------------

--
-- Table structure for table `followed`
--

CREATE TABLE `followed` (
  `id` int(11) NOT NULL,
  `User_ID` varchar(100) NOT NULL,
  `Followed_ID` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `followed`
--

INSERT INTO `followed` (`id`, `User_ID`, `Followed_ID`) VALUES
(1, 'MFU4CQDRYG', 'QKZ8CJOTIZ'),
(9, 'LPJ41OOMNB', 'QKZ8CJOTIZ');

-- --------------------------------------------------------

--
-- Table structure for table `news`
--

CREATE TABLE `news` (
  `Srno` int(11) NOT NULL,
  `User_ID` varchar(100) NOT NULL,
  `News_ID` varchar(150) NOT NULL,
  `Thumbnail` varchar(2048) DEFAULT NULL,
  `Title` varchar(100) DEFAULT NULL,
  `Description` text DEFAULT NULL,
  `Location` varchar(10000) DEFAULT NULL,
  `Tag` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `news`
--

INSERT INTO `news` (`Srno`, `User_ID`, `News_ID`, `Thumbnail`, `Title`, `Description`, `Location`, `Tag`, `Date`) VALUES
(2, 'QKZ8CJOTIZ', 'XSI24V7YA7NMYQIDO9CTJ44BOEO5BQ', 'https://images.indianexpress.com/2021/06/MF-Husain-sketch.jpg', 'Pakistani singer Bilal Maqsood remembers MF Husain with this breathtaking sketch made by son', 'Remembering Maqbool Fida Husain, better known as M F Husain, on his 10th death anniversary this month, Pakistani guitarist Bilal Maqsood shared a heartwarming note on Instagram.\r\n\r\nThe founding member of former music band Strings shared three pictures that showed his son, Mikail, with Husain when the former was just over eight years old.\r\n\r\nYoung Mikail can be seen sitting across the celebrated artist and sketching him with unwavering attention', 'Pakistan', 'Culture', '2021-06-23'),
(3, 'QKZ8CJOTIZ', 'BXMOAS2PIHFT2CPC4NXQJGRDUBPM9Y', 'https://bsmedia.business-standard.com/_media/bs/img/article/2021-05/28/full/1622147174-8184.jpg', 'Stocks to watch: RIL, Shyam Metalics, Sona Comstar, ONGC, Ashok Leyland', 'Nifty futures on SGX traded 25 points higher at 15,720 around 8.45 am, indicating a positive start for the benchmark indices on Thursday.\r\n\r\nHere are the top stocks to track today:\r\n\r\n\r\nReliance Industries: The 44th Annual General Meeting (AGM) of Reliance Industries (RIL) will be the most keenly tracked event on Thursday, where the company is touted to spell out its plans for the oil-to-chemical (O2C) telecom, digital and retailing verticals, according to analysts. The AGM begins at 2 PM. READ MORE\r\n\r\nNew listing: The shares of Shyam Metalics and Sona Comstar are slated to list on the bourses on Thursday. A strong debut is on the cards for Shyam Metalics while Sona Comstar is likely to witness a muted listing, suggest grey market trends.\r\n\r\nResults today: A total of 97 companies, including ONGC, Ashok Leyland, Mishra Dhatu Nigam, and West Coast Paper Mills are scheduled to be released on Thursday.\r\n\r\nTata Motors said Guenter Butschek will step down as its MD and CEO with effect from June 30. He will, however, continue as a consultant to the company till the end of this fiscal year.\r\n\r\nApollo Hospitals Enterprise reported a consolidated net profit of Rs 169.89 crore for the March quarter of FY21 as compared to Rs 209.60 crore in the year-ago quarter. Consolidated revenue stood at Rs 2,867.95 crore in the quarter under review.\r\n\r\nGodawari Power: Government of India, Ministry of Environment & Forests & Climate Change, Impact Assessment Division has accorded its environment clearance for enhancement of iron ore production capacity from 1.405 MTPA to 2.35 MTPA in Ari Dongri Iron Ore Mines at Chhattisgarh, and for setting up of beneficiation plant of 0.6 MTPA capacity.\r\n\r\nVardhman Steel Limited has been granted the long-awaited Environmental Clearance for expansion of capacity at its existing plant in Ludhiana, upto 2,80,000 tons per annum of rolled production.\r\n\r\nSpeciality Restaurants reported consolidated profit of Rs 8.43 crore in Q4FY21 against loss of Rs 37.11 crore in Q4FY20. Revenue fell to Rs 65.42 crore.\r\n\r\nAllcargo Logistics reported consolidated profit at Rs 5.91 crore in Q4FY21 against Rs 54.06 crore in Q4FY20. Revenue jumped to Rs 3,349.31 crore from Rs 1,870.96 crore in the year-ago quarter\r\n\r\nOrchid Pharma: Promoter Dhanuka Laboratories proposed to sell 32,80,115 equity shares, representing 8.04 per cent of total paid-up equity via offer for sale, on June 24 and June 25.\r\n\r\nJaypee Infratech: Mumbai-based Suraksha Group has received the approval of the committee of creditors (CoC) to take over bankrupt real estate firm Jaypee Infratech, with more than 98 per cent of votes in favour of its resolution plan.', 'India', 'Business', '2021-06-23'),
(4, 'QKZ8CJOTIZ', 'NO5YVTKWW1OA2G80BIB3U7670UXC9B', 'https://www.sciencenews.org/wp-content/uploads/2021/06/062321_JC_mountain-cat_feat.jpg', 'Chinese mountain cats swap DNA with domestic cats, but aren’t their ancestors', 'Pet cats’ Y chromosomes hold clues about these encounters, carrying genes that can enter the gene pool only through mountain cat fathers. Male Chinese mountain cats seem to sneak into villages and mate with female housecats, not the other way around, Luo says. But her team isn’t just looking at the cats’ genetics to understand their history. In Scotland, the genetic distinctiveness of European wildcats has been nearly wiped out by breeding with feral cats. Luo and her colleagues suspected they might find similar effects in Chinese mountain cats.\r\n\r\nThe team didn’t detect domestic cats infiltrating mountain cat populations. But that doesn’t mean it isn’t happening. With more DNA samples, future work may reveal genes are already flowing both ways. “I’m not convinced that this is going in only one direction,” says Eva-Maria Geigl, a paleogeneticist at CNRS in Paris.\r\n\r\nModern interbreeding could threaten Chinese mountain cat conservation in the long run. Domestic cats’ genes could dilute or override traits that make mountain cats well adapted to high altitudes, Luo says.', 'China', 'Science', '2021-06-23'),
(7, 'QKZ8CJOTIZ', 'KJ4LX3VHUU0HTGQEKUTCW8H9UB87F0', 'https://static.toiimg.com/thumb/msid-83787939,imgsize-401312,width-400,resizemode-4/83787939.jpg', 'Coronavirus News Highlights: Over 50 lakh vaccinated on Day 3 of new vaccine plan; India’s cumulativ', 'Covid-19 Vaccine Registration in India Highlights, Coronavirus Cases in India Tracker, Covid-19 India June 23 Update: It seems the Covid-19 second wave is behind us now as India has been witnessing below 1 lakh new Covid-19 cases for the past 15 days. On Tuesday, India reported below 50,000 new coronavirus infections after 91 days. The Covid-19 situation has improved but the emergence of new variants could pose serious threats in the coming days.\r\n\r\nThe Union Health Ministry has categorised the Delta Plus variant of the novel coronavirus as a ‘variant of concern’. India is among the 10 countries (USA, UK, Portugal, Switzerland, Japan, Poland, Nepal, China, and Russia) where the Delta Plus variant has been detected. It has been found in three states— Maharashtra, Kerala, and Madhya Pradesh— so far. The Health Ministry has already issued alerts and directed states to take immediate containment measures where the variant has been found. According to Union Health Secretary Rajesh Bhushan, the Delta Plus variant has been detected in 22 samples across six districts in the country. “Sixteen of them have found in Jalgaon and Ratnagiri districts in Maharashtra; the remaining have been detected in Kerala (Palakkad and Pathanamthitta) and Madhya Pradesh (Bhopal and Shivpuri)… But we don’t want this to assume significant proportions,” Bhushan said at a Covid-19 briefing of the ministry of health and family welfare on Tuesday.\r\n\r\nIn the meanwhile, the ongoing vaccination drive has picked up the pace. According to the reports, on Day 2 of the new vaccination policy more than 50 lakh doses having been administered till late evening. In the 2 days of the new plan, 1.39 crore people get vaccinated. On Monday, India saw 88.09 lakh doses being administered. With the threat of the Delta Plus variant and India unlocking, the government needs to increase the pace of vaccination to protect itself from another deadly wave. Several states/UTs like Delhi, Gujarat, West Bengal, Telangana, and Kerala have already started preparation for a possible third wave by strengthening health infrastructure.\r\n\r\nIndia reported 50,848 new Covid-19 cases in the last 24 hours, taking the overall tally to over 30 million, according to Union Health Ministry data on Wednesday. The death toll also climbed to 3,90,660 with 1,358 fresh fatalities. The active Covid-19 cases in the country further declined to 6, 43,194 and now accounted for 2.14 percent of the total infections, while the national recovery rate has improved to 96.56 per cent, the Health Ministry said.\r\n', 'India', 'Technology', '2021-06-24'),
(8, 'LPJ41OOMNB', 'TWGFTUBJPWWGBTHGMRVMD4H934K4FG', 'https://th.thgim.com/news/national/78sg5m/article34948380.ece/ALTERNATES/FREE_660/2ab8af73-9a1c-4115-9936-763d60f258cejpg', 'PM Modi meets Jammu and Kashmir leaders', 'A crucial meeting to chalk out the future political course of action in Jammu and Kashmir, convened by Prime Minister Narendra Modi, began on Thursday with the attendance of 14 leaders, including four former chief ministers.\r\n\r\nThe meeting is the first between the Centre and mainstream Jammu and Kashmir politicians after the abrogation of Article 370 and the division of the erstwhile state into two union territories in August 2019.\r\n\r\nUnion Home Minister Amit Shah, Jammu and Kashmir Lieutenant Governor Manoj Sinha and National Security Advisor Ajit Doval were among those attended the meeting at the prime minister’s residence.\r\n\r\nThe four former chief ministers of Jammu and Kashmir who attended the meeting are Farooq Abdullah, Ghulam Nabi Azad, Omar Abdullah and Mehbooba Mufti.\r\n\r\n\r\n\"I will keep my agenda in the meeting and then talk to you,\" Farooq Abdullah said before the meeting started.\r\n\r\nAsked about PDP chief Mehbooba\'s comments that India should initiate dialogue with Pakistan, the NC leader said, \"Mehbooba ji is the president of her party. She has the right to speak. I have my own. I don\'t want to bring in Pakistan. I am going to talk to our own prime minister.\"\r\n\r\n\"If India can talk to the Taliban in Doha (Qatar), why not Pakistan,\" Ms. Mehbooba had said earlier. \r\n\r\nWith no agenda announced for the meeting, the leaders from Jammu and Kashmir said they have come with an open mind.\r\n\r\n\"We have not been given an agenda. We will be attending the meeting to know what the Centre is offering,” said CPI(M) leader Mohammad Yousuf Tarigami, who is also a spokesman of the six-party People\'s Alliance for Gupkar Declaration (PAGD).\r\n\r\nMr. Tarigami is among the 14 Jammu and Kashmir leaders invited to the all-party meeting at the prime minister\'s residence.\r\n\r\nP K Mishra, principal secretary to the prime minister, and Union Home Secretary Ajay Bhalla were in attendance as well.', 'India', 'Politics', '2021-06-24'),
(9, 'LPJ41OOMNB', 'Z9NIY3HVLBWBI5XG5DI54DU637FIKM', 'https://www.traveldailynews.com/assets/thumbnails/9f/9f8fca7a41b064d7f59c77948fe8f24a.jpg', 'World’s top hotel brands lose nearly $23 billion in brand value', 'As holidays are cancelled and people are instructed to work from home, the hospitality sector has reached an almost complete standstill both from tourism, as well as corporate travel. As a result, the total value of the top 50 most valuable hotel brands has decreased 33% year-on-year, down from US$70.2 billion in 2020 to US$47.4 billion in 2021, according to the latest Brand Finance Hotels 50 2021 report.\r\n\r\nSavio D’Souza, Valuation Director, Brand Finance, commented: “The hotels sector has completely ground to a halt over the previous year, the repercussions of which are demonstrated by the sharp brand value declines for almost all of the top 50 most valuable hotel brands. The sector is a resilient one, however. As the world begins to open back up again, we are already witnessing a strong improvement in bookings and occupancy levels across the board, showcasing the strength of brands despite the turmoil of the last year.”\r\n\r\nHilton retains top spot\r\nHilton once again is the world’s most valuable hotel brands, despite recording a 30% drop in brand value to US$7.6 billion. While Hilton’s revenue has taken a significant hit since the outbreak of the pandemic, the brand is showing confidence in its growth strategy, announcing a further 17,400 rooms to its pipeline, bringing the total to over 400,000 new rooms planned – an uplift of 8% on the previous year. Hilton also boasts the most valuable hotel portfolio, with its seven brands that feature in the ranking reaching a total brand value of US$13.8 billion.\r\n\r\nHilton’s rival, Marriott (down 60% to US$2.4 billion), has dropped down to 5th spot from 2nd, after losing more than half of its brand value. Last year, the brand’s worldwide revenue available per room was down 60% from 2019 and global occupancy was just 36% for the year.\r\n\r\nHyatt checks into 2nd spot\r\nBucking the sector trend as one of only two brands in the ranking to record brand value growth is Hyatt (up 4% to US$4.7 billion). Despite the pandemic impacting its performance greatly, Hyatt’s net rooms growth has been strong, opening 72 hotels and entering 27 new markets. Furthermore, the brand has continued to execute new signings to maintain its pipeline, which represent over 40% growth of existing hotel rooms in the future.\r\n\r\nTaj is sector’s strongest\r\nIn addition to measuring overall brand value, Brand Finance also evaluates the relative strength of brands, based on factors such as marketing investment, customer familiarity, staff satisfaction, and corporate reputation. According to these criteria, Taj (brand value US$296 million) is the world’s strongest hotel brand, with a Brand Strength Index (BSI) score of 89.3 out of 100 and a corresponding AAA brand strength rating.\r\n\r\nRenowned for its world-class customer service, the luxury hotel chain scores very well in our Global Brand Equity Monitor for consideration, familiarity, recommendation, and reputation especially across its home market of India.  \r\n\r\nTaj’s successful implementation of its 5-year plan - which focuses on selling non-core assets, becoming less ownership driven and reducing dependence on the luxury space – followed by the speedy adoption of its new R.E.S.E.T 2020 strategy, which provides a transformative framework to help the brand overcome the challenge of the pandemic, has contributed to the brand’s re-entrance into the ranking for the first time since 2016 in 38th spot.\r\n\r\nBrand Finance Leisure & Tourism 10 2021\r\nAlongside analysing the world’s most valuable hotel brands, Brand Finance also ranks the top 10 most valuable brands in the wider leisure & tourism industry. This year, the total value of the world’s top 10 most valuable leisure & tourism brands has declined by 40%.\r\n\r\nDespite booking.com recording a 19% brand value loss to US$8.3 billion, it has overtaken Airbnb (down 67% to US$3.4 billion) and Trip.com Group (down 38% to US$3.5 billion) to become the most valuable leisure & tourism brand in the world. The fastest falling brand this year, Airbnb, cut a quarter of its workforce last year, and was forced to scale back on new initiatives that it had in the pipeline, including luxury resorts and flights.\r\n\r\nHappy Valley (down 37% to US$1.2 billion) is the sector’s strongest brand, with a BSI score of 84.1 out of 100 and a corresponding AAA- brand strength rating.\r\n\r\nThree new entrants in ranking\r\nThere are three new entrants into the ranking this year, AMC Theatres (brand value US$1.8 billion) in 7th, Priceline (brand value US$1.5 billion) in 8th, and Shenzhen Overseas Chinese Town (brand value to US$1.3 billion) in 9th.\r\n\r\nThe world’s largest cinema chain, AMC, has struggled as cinemas were shut amid global lockdowns. The brand will be hoping their fortunes will reverse as customers slowly start to return to the big screen and blockbusters that have been delayed are finally released. \r\n\r\nThe three new entrants have pushed out three cruise brands, which have dropped out the ranking this year: Royal Caribbean International, Norwegian Cruise, and Carnival Cruise Lines.\r\n\r\nBrand Finance Hotels 50 2021 report \r\nLeisure & Tourism 10 2021 ranking \r\n \r\n\r\n\r\n\r\n', 'AMERICA', 'Travel', '2021-06-24'),
(10, 'LPJ41OOMNB', 'AMBFYP9TO34V8A2PJ22HF5ISR851YG', 'https://images.indianexpress.com/2021/06/Mukesh-Ambani-RIL-AGM.jpg', 'Reliance AGM 2021 Highlights: Saudi Aramco Chairman Yasir Al-Rumayyan joins RIL board', 'RIL AGM 2021 Highlights: Reliance Industries (RIL) Chairman Mukesh Ambani on Thursday announced that Saudi Aramco Chairman and Governor of the kingdom’s wealth fund Public Investment Fund Yasir Al-Rumayyan will be joining the RIL board as an independent director.\r\n\r\nSpeaking at the conglomerate’s 44th annual general meeting (AGM), the second virtual AGM following the coronavirus pandemic, Ambani said that Al-Rumayyan’s joining also marks the beginning of internationalisation of Reliance.\r\n\r\n“I am sure we will immensely benefit from his rich experience with one of the world’s largest companies, and also one of the largest sovereign wealth funds in the world,” Ambani said.\r\n\r\n\r\nIt was earlier rumoured that Al-Rumayyan may be inducted on the board of RIL.\r\n\r\nApart from this, Ambani during his AGM speech announced RIL’s plans for the new energy business. He said that RIL has established the Reliance New Energy Council with some of the finest minds, globally. The company has started work on developing the Dhirubhai Ambani Green Energy Giga Complex on 5,000 acres in Jamnagar.\r\n\r\n“It will be amongst the largest such integrated renewable energy manufacturing facilities in the world,” he said. RIL’s overall initial investment from its own internal resources in the New Energy business will be Rs 75,000 (over $10 billion) crore in 3 years.\r\n\r\nSpeaking on RIL’s retail arm, Ambani said despite challenging and restrictive operating conditions, Reliance Retail continued to deliver industry-leading returns. The company added 1,500 new stores, which is amongst the largest retail expansion undertaken by any retailer during this period, taking their store count to 12,711.\r\n\r\nHe said that Reliance Retail is committed to growing its business so that it is among the top 10 retailers globally. “I am confident that Reliance Retail is on a hyper-growth trajectory to grow at least 3x in the next 3-5 years,” Ambani said.', 'India', 'Technology', '2021-06-24'),
(11, 'LPJ41OOMNB', 'WXPPL5DD7E5N3NCIAD5LYGLHDPHRD7', 'https://ichef.bbci.co.uk/news/976/cpsprodpb/174FE/production/_119068459_068181064.jpg', 'Britney Spears speaks out against \'abusive\' conservatorship in court', 'US pop star Britney Spears has launched a blistering attack on the \"abusive\" conservatorship that has controlled her life for 13 years.\r\n\r\nShe said she was traumatised and cried every day, telling a judge in Los Angeles: \"I just want my life back\".\r\n\r\nSpears, 39, also said she had been denied the right to have more children and was put on the psychiatric drug lithium against her wishes.\r\n\r\nHer father was granted control over her affairs by court order in 2008.\r\n\r\nThe order was granted after the star was put in hospital amid concerns over her mental health, and it has been extended for more than a decade since.\r\n\r\nBritney Spears: Everything she said in court\r\nTimberlake leads outpouring of support for Britney\r\nThe conservatorship case explained\r\nThe special hearing on Wednesday was the first time Spears has spoken in open court about her case. Los Angeles Superior Court Judge Brenda Penny thanked Spears for her \"courageous\" words during the proceedings.\r\n\r\nIt followed much speculation about the pop star\'s situation, with fans eagerly combing her social media output for clues. A fan-led movement, known as #FreeBritney, has campaigned for her legal freedom for years.', 'AMERICA', 'Politics', '2021-06-24'),
(12, 'LPJ41OOMNB', 'NPPLRZDOAGFDVEFD65U56DF3VC3BYU', 'https://ichef.bbci.co.uk/news/976/cpsprodpb/124C3/production/_119074947_gettyimages-1324249337.jpg', 'Covid-19: Europe braces for surge in Delta variant', 'German Chancellor Angela Merkel has warned that Europe is \"on thin ice\" as the Delta variant of Covid spreads on the continent.\r\n\r\nHer warning came as EU health officials said the variant would account for 90% of the bloc\'s cases by late August.\r\n\r\nThe spread could disrupt plans for lifting restrictions during the summer.\r\n\r\nThe Alpha variant, first discovered in the UK, hit Europe hard early this year and Delta, now dominant in the UK, is thought 40%-60% more transmissible.\r\n\r\nAndrea Ammon, the director of the European Centre for Disease Prevention and Control (ECDC), said on Wednesday that the spread of the Delta variant showed the importance of speeding up vaccinations in Europe, as \"preliminary data shows that it can also infect individuals that have received only one dose of the currently available vaccines\".\r\n\r\nTwo doses offered \"high protection\" against the Delta (B.1.617.2) variant, she added.\r\n\r\nHeadache and runny nose linked to Delta variant\r\nHow is Europe lifting lockdown restrictions?\r\nScientists say too early to tell risk of Delta plus variant\r\nDelta, first identified in India, now accounts for almost all new infections in the UK.\r\n\r\nOn Wednesday Mrs Merkel called for a more co-ordinated EU response and said all member states should quarantine arrivals from the UK considering the dangers of the spread of Delta.\r\n\r\nThe UK is not on the EU\'s list of safe countries, due to the spread of Delta, but that list is not binding on member states.\r\n\r\nUK Prime Minister Boris Johnson has said that while fully vaccinating people offered \"a good way forward\" for resuming travel, this summer would not be \"like every other. This is going to be a more difficult summer to take a holiday\".\r\n\r\nHere is how different parts of Europe are dealing with the threat of Delta.', 'German', 'Health', '2021-06-24');

-- --------------------------------------------------------

--
-- Table structure for table `profile_info`
--

CREATE TABLE `profile_info` (
  `id` int(11) NOT NULL,
  `ID_Number` varchar(10) DEFAULT NULL,
  `Name` varchar(150) DEFAULT NULL,
  `Bio` varchar(1000) DEFAULT NULL,
  `Country` varchar(50) DEFAULT NULL,
  `Phone_no` varchar(15) DEFAULT NULL,
  `Email` varchar(150) DEFAULT NULL,
  `Profile_img` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `profile_info`
--

INSERT INTO `profile_info` (`id`, `ID_Number`, `Name`, `Bio`, `Country`, `Phone_no`, `Email`, `Profile_img`) VALUES
(3, 'QKZ8CJOTIZ', 'Krishna Pal', 'hola', 'India', '+918318031071', 'Krishnapal2545@gmail.com', 'kk.png'),
(4, 'MFU4CQDRYG', 'Sumit Rajendra Vishwakarama', 'hiii', 'America', '8828081171', 'SumitVish@gmail.com', NULL),
(5, 'RW8AG9RN38', 'Chetan Prajapat', 'my name is chetna I love coding', 'Africa', '+918318031071', 'Chetan@gmail.com', 'user3.png'),
(6, 'LPJ41OOMNB', 'Meera Devi Pal', 'Hii I am mother of Mr. KrishnaKumar Pal', 'Bangladesh', '9819753541', 'Palmeera2087@gmail.com', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `reading_list`
--

CREATE TABLE `reading_list` (
  `id` int(11) NOT NULL,
  `News_ID` varchar(30) DEFAULT NULL,
  `User_ID` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reading_list`
--

INSERT INTO `reading_list` (`id`, `News_ID`, `User_ID`) VALUES
(1, 'XSI24V7YA7NMYQIDO9CTJ44BOEO5BQ', 'QKZ8CJOTIZ'),
(2, 'BXMOAS2PIHFT2CPC4NXQJGRDUBPM9Y', 'QKZ8CJOTIZ'),
(3, 'NPPLRZDOAGFDVEFD65U56DF3VC3BYU', 'QKZ8CJOTIZ'),
(4, 'WXPPL5DD7E5N3NCIAD5LYGLHDPHRD7', 'QKZ8CJOTIZ');

-- --------------------------------------------------------

--
-- Table structure for table `user_credential`
--

CREATE TABLE `user_credential` (
  `ID_Number` varchar(10) NOT NULL,
  `Phone_Number` varchar(15) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_credential`
--

INSERT INTO `user_credential` (`ID_Number`, `Phone_Number`, `Username`, `Password`) VALUES
('LPJ41OOMNB', '12345678', 'Meera', 'Tata'),
('MFU4CQDRYG', '34567', 'KK_PL', 'Tata'),
('QKZ8CJOTIZ', '34567', 'krishna', 'Tata'),
('RW8AG9RN38', '8318031071', 'Chetan', 'Tata');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `followed`
--
ALTER TABLE `followed`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`Srno`);

--
-- Indexes for table `profile_info`
--
ALTER TABLE `profile_info`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ID_Number` (`ID_Number`);

--
-- Indexes for table `reading_list`
--
ALTER TABLE `reading_list`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_credential`
--
ALTER TABLE `user_credential`
  ADD UNIQUE KEY `ID_Number` (`ID_Number`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `followed`
--
ALTER TABLE `followed`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `news`
--
ALTER TABLE `news`
  MODIFY `Srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `profile_info`
--
ALTER TABLE `profile_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `reading_list`
--
ALTER TABLE `reading_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `news`
--
ALTER TABLE `news`
  ADD CONSTRAINT `news_ibfk_1` FOREIGN KEY (`User_ID`) REFERENCES `profile_info` (`ID_Number`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
