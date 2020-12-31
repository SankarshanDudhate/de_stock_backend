-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 29, 2020 at 06:08 PM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ilx`
--

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `products` json DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `name`) VALUES
(1, 'Cutting Tools'),
(2, 'Measuring Instruments'),
(3, 'Plates'),
(4, 'Sheets'),
(5, 'Pipes'),
(6, 'Packaging Material'),
(7, 'Office Equipment'),
(8, 'Tools'),
(9, 'Wires and Cables'),
(10, 'Hardware'),
(11, 'Fastne'),
(12, 'Flanges'),
(13, 'Gearbox'),
(14, 'Electrical Heaters'),
(15, 'Paint'),
(16, 'Circuit Breakers'),
(17, 'Electrical switches'),
(18, 'Valves'),
(19, 'Oils and Lubricants'),
(20, 'Filters'),
(21, 'Hose Pipe'),
(22, 'Insulation Material'),
(23, 'Motors'),
(24, 'Abrasives'),
(25, 'Rubber Parts'),
(26, 'Bearing'),
(27, 'Safety Equipments'),
(28, 'Hydrolic Cylinders'),
(29, 'Hydrolic Accessories'),
(30, 'Pneumatic Cylinders'),
(31, 'Pneumatic Accessories '),
(32, 'Industrial Belts and V Belts'),
(33, 'Welding Consumables'),
(34, 'Wire Mesh & Gratings'),
(35, 'Pipe Fittings'),
(36, 'Ropes'),
(37, 'Lifting Equipments'),
(38, 'Electrical Fittings'),
(39, 'Trolley Wheels'),
(40, 'Lifting Hooks, chains and clamps'),
(41, 'Springs'),
(42, 'Adhesive Tapes'),
(43, 'Plumbing Material');

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `pan_no` varchar(10) DEFAULT NULL,
  `gst_no` varchar(20) DEFAULT NULL,
  `factory_address` varchar(200) DEFAULT NULL,
  `factory_latlong` json DEFAULT NULL,
  `office_address` varchar(200) DEFAULT NULL,
  `office_latlong` json DEFAULT NULL,
  `what_you_sell` varchar(500) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`id`, `name`, `pan_no`, `gst_no`, `factory_address`, `factory_latlong`, `office_address`, `office_latlong`, `what_you_sell`) VALUES
(1, 'Shit Corp', 'CNWPD3930M', '11CNWPD3930M1Z5', 'Lokamanya Nagar, Parbhani, Parbhani, Maharashtra, - 431401', '"{\\"lat\\": \\"19.26660858292735\\", \\"long\\": \\"76.78756982088089\\"}"', 'Lokamanya Nagar, Parbhani, Parbhani, Maharashtra, - 431401', NULL, 'We sell shit'),
(2, 'Hitesh & Co.', 'CNWPD3930M', '22CNWPD3930M1Z5', 'asnfkan, afklklansf opp dngknweng, kmkjgi - 411057', NULL, 'asnfkan, afklklansf opp dngknweng, kmkjgi - 411057', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `contact_person`
--

CREATE TABLE `contact_person` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_no` varchar(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contact_person`
--

INSERT INTO `contact_person` (`id`, `name`, `email`, `phone_no`) VALUES
(1, 'Tanmay Patil', 'tp@gmail.com', '9881266239');

-- --------------------------------------------------------

--
-- Table structure for table `payment_methods`
--

CREATE TABLE `payment_methods` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `card_number` varchar(100) DEFAULT NULL,
  `card_name` varchar(100) DEFAULT NULL,
  `expiry_date` date DEFAULT NULL,
  `card_type` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `details` varchar(5000) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `subCategory_id` int(11) DEFAULT NULL,
  `available` tinyint(1) DEFAULT NULL,
  `maxQty` int(11) DEFAULT NULL,
  `unit` varchar(100) DEFAULT NULL,
  `specifications` json DEFAULT NULL,
  `latLongs` json DEFAULT NULL,
  `address` varchar(200) NOT NULL,
  `price` int(11) DEFAULT NULL,
  `priceDisclose` tinyint(1) DEFAULT NULL,
  `views` int(11) DEFAULT NULL,
  `soldCount` int(11) DEFAULT NULL,
  `wishlisted` int(11) DEFAULT NULL,
  `enquiries` json DEFAULT NULL,
  `publishedDate` date DEFAULT NULL,
  `expiryDate` date DEFAULT NULL,
  `expired` tinyint(1) NOT NULL DEFAULT '0',
  `user_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `name`, `details`, `category_id`, `subCategory_id`, `available`, `maxQty`, `unit`, `specifications`, `latLongs`, `address`, `price`, `priceDisclose`, `views`, `soldCount`, `wishlisted`, `enquiries`, `publishedDate`, `expiryDate`, `expired`, `user_id`) VALUES
(1, 'Cast Iron Gears 15 inch 1050 rounded egdes - PVC', 'Gears can be made of all sorts of materials, including many types of steel, brass, bronze, cast iron, ductile iron, aluminum, powdered metals, and plastics.', 4, 0, 0, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.85669999999999}"', '103-104 Pithampur main road near indore, MP', 25000, 1, 5, 0, 0, '"[{\\"enquiry\\": \\"Some short and sweet question?\\", \\"buyer_id\\": \\"2\\", \\"date\\": \\"2019-01-11\\", \\"replied\\": true, \\"quantity\\": \\"1000 pieces\\", \\"reply\\": {\\"date\\": \\"2020-09-22\\", \\"seller_reply\\": \\"It will cost you a fortune and you can pick it up however you like. Also no time will be suitable for me.\\"}}]"', '2020-07-20', '2020-10-20', 0, 1),
(2, 'Carolyn Jackson', 'Blanditiis voluptates similique architecto. Inventore eius in fugiat doloremque ducimus ab.', 32, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 10000, 1, 0, 0, 17, '"[{\\"enquiry\\": \\"Asking some stupid question that takes a couple of line... You wouldd think it is easy to write shit without thinking but it is not as easy as you think...\\", \\"buyer_id\\": \\"2\\", \\"date\\": \\"2020-09-28\\", \\"replied\\": false, \\"quantity\\": \\"400 pieces\\"}]"', '2020-07-20', '2020-10-20', 0, 1),
(3, 'Corey Martin', 'Quod explicabo in facilis corporis commodi dolore. Expedita ipsum expedita qui illo voluptates. Incidunt omnis officia cum. Provident debitis delectus illum.', 19, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 17000, 1, 0, 0, 0, '"[{\\"enquiry\\": \\"Ask away bitches!\\", \\"buyer_id\\": \\"2\\", \\"date\\": \\"2020-09-28\\", \\"replied\\": false, \\"quantity\\": \\"400 pieces\\"}]"', '2020-07-20', '2020-10-20', 0, 1),
(4, 'Jade Stark', 'Sunt ipsum veniam mollitia officiis perspiciatis quo assumenda. Ducimus perspiciatis necessitatibus autem alias. Dolor repellat nihil quos doloremque. Amet aperiam qui.', 9, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 15000, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2),
(5, 'Jay Tate', 'Facilis autem quod sed. Tempore voluptatibus suscipit repudiandae. Consequatur ipsum repellat eos a.', 13, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 0, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2),
(6, 'Jade Williams', 'Delectus quaerat suscipit quia et. Magni ex vero inventore quo nam quod. Totam ad ad voluptatem. Tempora nisi corporis nostrum provident ratione.', 3, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 0, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2),
(7, 'Laura Mckinney', 'Quod eaque ipsam quasi.\nQuidem sed totam libero facilis exercitationem. Commodi accusantium dignissimos.', 9, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 0, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2),
(8, 'Diane Jones', 'Sed aliquam deleniti ex. Fuga eaque vel nemo unde ipsum culpa. Error aliquid culpa labore asperiores quisquam sunt.', 34, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 0, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2),
(9, 'Douglas Black', 'Itaque unde tempore quos illo est.\nOfficia qui voluptates ea. Exercitationem eum iste inventore veniam. Non aliquid deserunt et alias.', 40, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 0, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2),
(10, 'Michael Robinson', 'Eaque dolore pariatur totam tenetur voluptatem occaecati. Quo recusandae delectus repellat inventore debitis. Eaque odit quae totam ex.\nVitae itaque optio blanditiis. Ducimus eveniet ipsum natus.', 28, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 0, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2),
(11, 'Jennifer Hernandez', 'Quis placeat vitae inventore consequatur. Odio sit nobis debitis adipisci ullam. Tempore a nobis libero in.', 18, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 0, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2),
(12, 'Thomas Weeks', 'Totam qui repellendus quod. Vitae dolor voluptas laboriosam. Repudiandae aspernatur esse similique molestias. Saepe exercitationem nobis odio voluptatum.', 32, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 0, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2),
(13, 'Scott Scott', 'Odit harum dolore reprehenderit. Voluptates quae autem iure est magnam corrupti porro. Magni tempore adipisci pariatur quo fuga. In ad natus officiis quae.', 24, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 0, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2),
(14, 'Robert Williams', 'Laudantium iure dignissimos tempora numquam nam. Alias maiores cum eum adipisci necessitatibus debitis dicta. Placeat porro officiis quis.', 17, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 0, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2),
(15, 'Joann Robinson', 'Nostrum iste a alias quidem voluptate dolores. Corporis nemo repellat eaque in. Praesentium provident modi.', 33, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 0, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2),
(16, 'Edwin Knight', 'Nobis aut necessitatibus occaecati hic perferendis. Quam sit aspernatur aperiam mollitia non. Nam optio iste pariatur.', 23, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 0, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2),
(17, 'Jennifer Walker', 'Doloremque velit earum eos explicabo. Assumenda saepe esse quo consequuntur. Sed ad natus dolor facere.', 1, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 0, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2),
(18, 'Susan Chambers', 'Odit possimus aut adipisci aliquam ea corrupti. Excepturi officiis rerum totam laudantium. Accusantium inventore labore vitae corporis.', 42, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 0, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2),
(19, 'Robert Rose', 'Minima sunt deleniti ipsa inventore. Magni sit at laboriosam laborum nihil voluptatibus. Illo excepturi ipsa sit.', 27, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 0, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2),
(20, 'James Hughes', 'Fugit aperiam voluptatum quia aliquid corrupti architecto. Minima illo provident odit. Perferendis temporibus accusamus.', 15, 0, 1, 500, 'pieces', '"{\\"Material\\":\\"Cast iron\\",\\"Weight\\":\\"365 kg\\",\\"Dimensions\\":\\"46m x 34m x 45m\\"}"', '"{\\"lat\\":18.5204,\\"long\\":73.8567}"', '', 0, 1, 0, 0, 0, NULL, '2020-07-20', '2020-10-20', 0, 2);

-- --------------------------------------------------------

--
-- Table structure for table `sub_category`
--

CREATE TABLE `sub_category` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `category` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `temp_products`
--

CREATE TABLE `temp_products` (
  `id` int(11) NOT NULL,
  `products` json NOT NULL COMMENT 'Mediumtext to accomodate image base64 data',
  `user_id` int(11) NOT NULL,
  `order_id` varchar(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `temp_products`
--

INSERT INTO `temp_products` (`id`, `products`, `user_id`, `order_id`) VALUES
(2, '"[{\\"unit\\":\\"pieces\\",\\"name\\":\\"Steel Pipes\\",\\"description\\":\\"Stainless steel pipes that every house needs.\\",\\"dimensions\\":null,\\"material\\":null,\\"quantity\\":\\"450\\",\\"weight\\":null,\\"address\\":\\"Lokamanya Nagar, Parbhani, Parbhani, Maharashtra, - 431401\\",\\"location\\":\\"{lat: 19.266115477592923, long: 76.78576704114676}\\",\\"category\\":\\"Electrical Fittings\\",\\"images\\":[],\\"price\\":\\"6000\\",\\"disclose_price\\":false}]"', 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `id` int(11) NOT NULL,
  `order_id` varchar(50) NOT NULL,
  `reference_id` int(11) NOT NULL,
  `order_amount` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `status` varchar(20) NOT NULL,
  `message` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phoneNo` varchar(10) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `cart` int(11) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  `wishlist` json DEFAULT NULL,
  `enquiredProducts` json DEFAULT NULL,
  `adsAvailable` int(11) DEFAULT NULL,
  `company_id` int(11) NOT NULL DEFAULT '0',
  `contact_person_id` int(11) DEFAULT '0',
  `firebaseDeviceToken` tinytext NOT NULL,
  `shareableKey` varchar(1024) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `email`, `phoneNo`, `password`, `address`, `cart`, `type`, `wishlist`, `enquiredProducts`, `adsAvailable`, `company_id`, `contact_person_id`, `firebaseDeviceToken`, `shareableKey`) VALUES
(1, 'san dudhate', 'sd@gmail.com', '1234567890', 'Password', 'my permanent address', 0, 'buyer', '"[{\\"product_id\\": \\"2\\", \\"notes\\": \\"Another note\\"}]"', NULL, 0, 1, 1, 'fooFX7TBRSuh76m4iIdut6:APA91bFL6RmdyfD1zzTsu5XkS1-aeI3oNdHA4wO-SZCL5Y-fu5YwuNu5h5sbW_HnQ5G0zrxdJvKjdpiPko2krpQ4sMutvXtOtP9LPXiwkQrVAihzWlhoHltPMGE_JGlvFaiXQXyDMDoM', NULL),
(2, 'Marcus Ponce', 'paul14@white.com', '1234567890', 'Password', '599 Christopher Street Apt. 722\nJonathanmouth, GA 18824', 0, 'seller', NULL, '"[\\"1\\", \\"3\\", \\"2\\"]"', 0, 1, 1, 'fooFX7TBRSuh76m4iIdut6:APA91bFL6RmdyfD1zzTsu5XkS1-aeI3oNdHA4wO-SZCL5Y-fu5YwuNu5h5sbW_HnQ5G0zrxdJvKjdpiPko2krpQ4sMutvXtOtP9LPXiwkQrVAihzWlhoHltPMGE_JGlvFaiXQXyDMDoM', NULL),
(3, 'Michelle Green', 'egray@wilson.biz', '1234567890', 'Password', '3401 Sanchez Estate\nBrianberg, HI 61328', 0, 'buyer', NULL, NULL, 0, 1, 1, 'fooFX7TBRSuh76m4iIdut6:APA91bFL6RmdyfD1zzTsu5XkS1-aeI3oNdHA4wO-SZCL5Y-fu5YwuNu5h5sbW_HnQ5G0zrxdJvKjdpiPko2krpQ4sMutvXtOtP9LPXiwkQrVAihzWlhoHltPMGE_JGlvFaiXQXyDMDoM', NULL),
(4, 'Jermaine Flores', 'millerwhitney@gmail.com', '1234567890', 'Password', '218 Ortiz Locks Suite 323\nSouth Amy, MD 63222', 0, 'buyer', NULL, NULL, 0, 1, 1, 'fooFX7TBRSuh76m4iIdut6:APA91bFL6RmdyfD1zzTsu5XkS1-aeI3oNdHA4wO-SZCL5Y-fu5YwuNu5h5sbW_HnQ5G0zrxdJvKjdpiPko2krpQ4sMutvXtOtP9LPXiwkQrVAihzWlhoHltPMGE_JGlvFaiXQXyDMDoM', NULL),
(5, 'Brandi Newman', 'michael00@gmail.com', '1234567890', 'Password', '6741 Katie Plains\nMillerchester, TX 68827', 0, 'buyer', NULL, NULL, 0, 1, 1, 'fooFX7TBRSuh76m4iIdut6:APA91bFL6RmdyfD1zzTsu5XkS1-aeI3oNdHA4wO-SZCL5Y-fu5YwuNu5h5sbW_HnQ5G0zrxdJvKjdpiPko2krpQ4sMutvXtOtP9LPXiwkQrVAihzWlhoHltPMGE_JGlvFaiXQXyDMDoM', NULL),
(6, 'Joseph Schmidt', 'christie51@moore.com', '1234567890', 'Password', '98198 Huffman Shoal\nNew Shellychester, CT 02928', 0, 'buyer', NULL, NULL, 0, 1, 1, 'fooFX7TBRSuh76m4iIdut6:APA91bFL6RmdyfD1zzTsu5XkS1-aeI3oNdHA4wO-SZCL5Y-fu5YwuNu5h5sbW_HnQ5G0zrxdJvKjdpiPko2krpQ4sMutvXtOtP9LPXiwkQrVAihzWlhoHltPMGE_JGlvFaiXQXyDMDoM', NULL),
(10, 'Sankarshan Dudhate', 'sandudhate@gmail.com', '8788527771', 'san', '', 0, 'buyer', NULL, NULL, 0, 0, 0, 'fQRB4_2iROShLBkNO6iwZM:APA91bFryHbNyH81nyEjLphnp5WYINQ7rKrMN_TQE0ug7Dr7xqQXcAdH564HGErKlpj-TYlBuwq6jHr_RnamTFGxx1OLxwU7s3gcSyHoKbYo4O6YB9rpiug8qE38CboIUFFI90tmoan0', 'NLIaEaAmJYA35m3ChD5mbXTZakejji4Px/WJOLCT2kY=');

-- --------------------------------------------------------

--
-- Table structure for table `wishlist`
--

CREATE TABLE `wishlist` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `products` json DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contact_person`
--
ALTER TABLE `contact_person`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `payment_methods`
--
ALTER TABLE `payment_methods`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sub_category`
--
ALTER TABLE `sub_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `temp_products`
--
ALTER TABLE `temp_products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wishlist`
--
ALTER TABLE `wishlist`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;
--
-- AUTO_INCREMENT for table `company`
--
ALTER TABLE `company`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `contact_person`
--
ALTER TABLE `contact_person`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `payment_methods`
--
ALTER TABLE `payment_methods`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
--
-- AUTO_INCREMENT for table `sub_category`
--
ALTER TABLE `sub_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `temp_products`
--
ALTER TABLE `temp_products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `wishlist`
--
ALTER TABLE `wishlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
