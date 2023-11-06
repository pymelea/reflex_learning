import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Avatar, Box, Center, Heading, HStack, Image, Link, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Text, useColorMode, VStack } from "@chakra-ui/react"
import NextLink from "next/link"
import NextHead from "next/head"



export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const { colorMode, toggleColorMode } = useColorMode()
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents.map((e) => ({...e})))
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {`http://localhost:8000`}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <Box>
  <HStack sx={{"position": "sticky", "paddingX": "4px", "bg": "#0A3143", "paddingY": "10px", "zIndex": "999", "top": "0"}}>
  <Avatar name={`Lily Perera`} size={`sm`} src={`avatar.jpg`}/>
  <Text sx={{"height": "30px", "color": "#EFEFEF"}}>
  {`def pymelea_dev(args, kwargs):`}
</Text>
</HStack>
  <Center sx={{"width": "100vw", "height": "calc(100vh - 53px)"}}>
  <VStack sx={{"maxWidth": "600px"}}>
  <VStack sx={{"position": "sticky", "paddingX": "14px", "paddingY": "14px", "zIndex": "999"}}>
  <Avatar name={`Lily Perera`} size={`xl`} src={`photo.jpg`}/>
  <Text sx={{"fontSize": "1em", "paddingY": "0.5em"}}>
  {`@Pymelea`}
</Text>
  <Heading size={`sm`} sx={{"paddingY": "1em"}}>
  {`"Just a Latin American girl who love to code"`}
</Heading>
  <Text sx={{"paddingY": "0.3em"}}>
  {`Hi there! My name is Lily Perera and I a Software Engineer`}
</Text>
  <Text sx={{"paddingY": "0.3em"}}>
  {`I have been coding for 3 years working in Python, who enjoy learning every                 new day and improving my skills. I am always looking for new challenges,                and and I still feel I have a lot to learn. I like knowledge, solving problems                 and knowing how things work. Curious person who has always had desires to                 discover, which has led me to move constantly.
                `}
</Text>
  <Text sx={{"alignItems": "center", "paddingTop": "0.5em", "paddingY": "0.3em"}}>
  {` @Welcome to my website!`}
</Text>
</VStack>
  <VStack alignItems={`center`} sx={{"width": "100%"}}>
  <Heading sx={{"fontSize": "1.2em", "width": "100%", "paddingTop": "0.8em", "paddingBottom": "0.2em", "alignItems": "center"}}>
  {`Social media links`}
</Heading>
  <HStack alignItems={`center`} spacing={`2em`} sx={{"width": "400px", "height": "auto", "padding": "0.3em"}}>
  <Link as={NextLink} href={`https://github.com/pymelea`} isExternal={true}>
  <Image src={`icons8-github-50.png`}/>
</Link>
  <Link as={NextLink} href={`https://www.linkedin.com/in/pymelea/`} isExternal={true}>
  <Image src={`icons8-linkedin-50.png`}/>
</Link>
  <Link as={NextLink} href={`https://twitter.com/pymelea`} isExternal={true}>
  <Image src={`icons8-twitter-quadrado-50.png`}/>
</Link>
  <Link as={NextLink} href={`https://www.instagram.com/pymelea/`} isExternal={true}>
  <Image src={`icons8-instagram-50.png`}/>
</Link>
  <Link as={``} isExternal={true} sx={{"src": "CV_Lily_Perera.pdf"}}>
  <Image src={`icons8-pdf-50.png`}/>
</Link>
  <Link as={NextLink} href={`emailto:lilycapetillo86@gmail.com`} isExternal={true}>
  <Image src={`icons8-nova-mensagem-50.png`}/>
</Link>
</HStack>
</VStack>
</VStack>
</Center>
  <HStack sx={{"bg": "#0A3143", "paddingX": "4px", "paddingY": "12px", "position": "absolute", "zIndex": "999", "bottom": "0", "left": "0", "right": "0", "top": "auto", "alignItems": "center", "justifyContent": "center"}}>
  <Text sx={{"color": "#EFEFEF"}}>
  {`© 2023 Lily Perera`}
</Text>
  <Text sx={{"color": "#EFEFEF"}}>
  {`Made with Love&Code&Python`}
</Text>
  <Link as={NextLink} href={`https://reflex.dev/`} isExternal={true} sx={{"color": "#EFEFEF"}}>
  <Text>
  {`using Reflex`}
</Text>
</Link>
  <Link as={NextLink} href={`https://lilyperera.tech/projects`} isExternal={true} sx={{"color": "#EFEFEF"}}>
  <Text>
  {`Projects`}
</Text>
</Link>
  <Link as={NextLink} href={`emailto:lilycapetillo86@gmail.com`} isExternal={true} sx={{"color": "#EFEFEF"}}>
  <Text>
  {`Contact me`}
</Text>
</Link>
  <Link as={NextLink} href={`https://lilyperera.tech/about_me`} isExternal={true} sx={{"color": "#EFEFEF"}}>
  <Text>
  {`    About me`}
</Text>
</Link>
</HStack>
</Box>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
